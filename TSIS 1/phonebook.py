"""
PhoneBook – TSIS 1
Extended Contact Management (console application)
"""

import csv
import json
import sys
from datetime import datetime 

import psycopg2

from connect import get_connection

# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def clear():
    print("\n" + "=" * 60)


def pause():
    input("\nPress Enter to continue...")


def fmt_row(row):
    """Pretty-print one result row (tuple or dict-like)."""
    name, email, birthday, group, phones = row
    print(f"  Name    : {name}")
    print(f"  Email   : {email or '—'}")
    print(f"  Birthday: {birthday or '—'}")
    print(f"  Group   : {group or '—'}")
    print(f"  Phones  : {phones or '—'}")
    print()


# ─────────────────────────────────────────────────────────────────────────────
# CRUD helpers
# ─────────────────────────────────────────────────────────────────────────────

def add_contact(conn):
    """Insert a new contact (name, email, birthday, group) + first phone."""
    clear()
    print("── Add Contact ──")
    name = input("Name       : ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    email    = input("Email      : ").strip() or None
    birthday = input("Birthday (YYYY-MM-DD, blank to skip): ").strip() or None
    if birthday:
        try:
            datetime.strptime(birthday, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format.")
            return

    # Group
    groups = list_groups(conn)
    print("Groups:", ", ".join(f"{g[0]}:{g[1]}" for g in groups))
    group_name = input("Group name (blank = Other): ").strip() or "Other"

    phone      = input("Phone number : ").strip() or None
    phone_type = input("Phone type (home/work/mobile) [mobile]: ").strip() or "mobile"
    if phone_type not in ("home", "work", "mobile"):
        print("Invalid phone type.")
        return

    with conn:
        with conn.cursor() as cur:
            # upsert contact
            cur.execute(
                "CALL upsert_contact(%s, %s, %s::DATE)",
                (name, email, birthday),
            )
            # move to group
            cur.execute("CALL move_to_group(%s, %s)", (name, group_name))
            # add phone
            if phone:
                cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, phone_type))
    print(f'\nContact "{name}" saved.')


def list_groups(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id, name FROM groups ORDER BY name")
        return cur.fetchall()


def view_all(conn):
    """Show all contacts with pagination (next/prev/quit)."""
    clear()
    print("── All Contacts (paginated) ──")

    page_size = 5
    offset    = 0

    while True:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM paginate_contacts(%s, %s)",
                (page_size, offset),
            )
            rows = cur.fetchall()

        if not rows:
            if offset == 0:
                print("  No contacts found.")
            else:
                print("  No more contacts.")
                offset = max(0, offset - page_size)
            pause()
            return

        page_num = offset // page_size + 1
        print(f"\n  — Page {page_num} —")
        for row in rows:
            fmt_row(row)

        cmd = input("  [n]ext  [p]rev  [q]uit : ").strip().lower()
        if cmd == "n":
            if len(rows) < page_size:
                print("  Already on the last page.")
            else:
                offset += page_size
        elif cmd == "p":
            if offset == 0:
                print("  Already on the first page.")
            else:
                offset -= page_size
        elif cmd == "q":
            return
        else:
            print("  Unknown command.")


def search_menu(conn):
    clear()
    print("── Search Contacts ──")
    query = input("Enter name / email / phone fragment: ").strip()
    if not query:
        return

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM search_contacts(%s)", (query,))
        rows = cur.fetchall()

    if not rows:
        print("  No contacts found.")
    else:
        print(f"\n  Found {len(rows)} result(s):\n")
        for row in rows:
            fmt_row(row)
    pause()


def filter_by_group(conn):
    clear()
    print("── Filter by Group ──")
    groups = list_groups(conn)
    for g in groups:
        print(f"  {g[0]}. {g[1]}")
    choice = input("Enter group name: ").strip()

    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT c.name, c.email, c.birthday, g.name,
                   STRING_AGG(p.phone || ' (' || COALESCE(p.type,'?') || ')', ', ')
            FROM contacts c
            LEFT JOIN groups g ON g.id = c.group_id
            LEFT JOIN phones p ON p.contact_id = c.id
            WHERE g.name ILIKE %s
            GROUP BY c.name, c.email, c.birthday, g.name
            ORDER BY c.name
            """,
            (choice,),
        )
        rows = cur.fetchall()

    if not rows:
        print(f'  No contacts in group "{choice}".')
    else:
        print(f"\n  Contacts in group «{choice}»:\n")
        for row in rows:
            fmt_row(row)
    pause()


def search_by_email(conn):
    clear()
    print("── Search by Email ──")
    fragment = input("Email fragment (e.g. gmail): ").strip()
    if not fragment:
        return

    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT c.name, c.email, c.birthday, g.name,
                   STRING_AGG(p.phone || ' (' || COALESCE(p.type,'?') || ')', ', ')
            FROM contacts c
            LEFT JOIN groups g ON g.id = c.group_id
            LEFT JOIN phones p ON p.contact_id = c.id
            WHERE c.email ILIKE %s
            GROUP BY c.name, c.email, c.birthday, g.name
            ORDER BY c.name
            """,
            (f"%{fragment}%",),
        )
        rows = cur.fetchall()

    if not rows:
        print("  No contacts found.")
    else:
        for row in rows:
            fmt_row(row)
    pause()


def sort_contacts(conn):
    clear()
    print("── Sort Contacts ──")
    print("  1. By name")
    print("  2. By birthday")
    print("  3. By date added")
    choice = input("Sort by: ").strip()

    order_map = {"1": "c.name", "2": "c.birthday", "3": "c.created_at"}
    order = order_map.get(choice)
    if not order:
        print("Invalid choice.")
        pause()
        return

    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT c.name, c.email, c.birthday, g.name,
                   STRING_AGG(p.phone || ' (' || COALESCE(p.type,'?') || ')', ', ')
            FROM contacts c
            LEFT JOIN groups g ON g.id = c.group_id
            LEFT JOIN phones p ON p.contact_id = c.id
            GROUP BY c.name, c.email, c.birthday, g.name, c.created_at
            ORDER BY {order} NULLS LAST
            """
        )
        rows = cur.fetchall()

    if not rows:
        print("  No contacts.")
    else:
        for row in rows:
            fmt_row(row)
    pause()


def add_phone_menu(conn):
    clear()
    print("── Add Phone to Contact ──")
    name  = input("Contact name : ").strip()
    phone = input("Phone number : ").strip()
    ptype = input("Type (home/work/mobile) [mobile]: ").strip() or "mobile"

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))
        print("Phone added.")
    except Exception as e:
        print(f"Error: {e}")
    pause()


def move_group_menu(conn):
    clear()
    print("── Move Contact to Group ──")
    name  = input("Contact name : ").strip()
    group = input("Group name   : ").strip()

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("CALL move_to_group(%s, %s)", (name, group))
        print(f'Moved "{name}" to "{group}".')
    except Exception as e:
        print(f"Error: {e}")
    pause()


def delete_contact(conn):
    clear()
    print("── Delete Contact ──")
    print("  1. By name")
    print("  2. By phone")
    choice = input("Choose: ").strip()

    if choice == "1":
        name = input("Name: ").strip()
        with conn:
            with conn.cursor() as cur:
                cur.execute("CALL delete_contact_by_name(%s)", (name,))
        print(f'Contact "{name}" deleted.')
    elif choice == "2":
        phone = input("Phone: ").strip()
        with conn:
            with conn.cursor() as cur:
                cur.execute("CALL delete_contact_by_phone(%s)", (phone,))
        print(f'Contact with phone "{phone}" deleted.')
    else:
        print("Invalid choice.")
    pause()


# ─────────────────────────────────────────────────────────────────────────────
# Import / Export
# ─────────────────────────────────────────────────────────────────────────────

def export_json(conn):
    clear()
    print("── Export to JSON ──")
    filename = input("Filename [contacts.json]: ").strip() or "contacts.json"

    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT c.name, c.email,
                   TO_CHAR(c.birthday, 'YYYY-MM-DD') AS birthday,
                   g.name AS group_name,
                   JSON_AGG(
                       JSON_BUILD_OBJECT('phone', p.phone, 'type', p.type)
                   ) FILTER (WHERE p.phone IS NOT NULL) AS phones
            FROM contacts c
            LEFT JOIN groups g ON g.id = c.group_id
            LEFT JOIN phones p ON p.contact_id = c.id
            GROUP BY c.name, c.email, c.birthday, g.name
            ORDER BY c.name
            """
        )
        rows = cur.fetchall()

    data = []
    for name, email, birthday, group, phones in rows:
        data.append({
            "name":     name,
            "email":    email,
            "birthday": birthday,
            "group":    group,
            "phones":   phones or [],
        })

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Exported {len(data)} contacts → {filename}")
    pause()


def import_json(conn):
    clear()
    print("── Import from JSON ──")
    filename = input("Filename [contacts.json]: ").strip() or "contacts.json"

    try:
        with open(filename, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        pause()
        return
    except json.JSONDecodeError as e:
        print(f"JSON error: {e}")
        pause()
        return

    inserted = skipped = overwritten = 0

    for contact in data:
        name     = contact.get("name", "").strip()
        email    = contact.get("email")
        birthday = contact.get("birthday")
        group    = contact.get("group") or "Other"
        phones   = contact.get("phones") or []

        if not name:
            continue

        # Check duplicate
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
            exists = cur.fetchone()

        if exists:
            ans = input(f'  "{name}" already exists. [s]kip / [o]verwrite: ').strip().lower()
            if ans != "o":
                skipped += 1
                continue
            # delete old phones, then upsert
            with conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "DELETE FROM phones WHERE contact_id = (SELECT id FROM contacts WHERE name=%s)",
                        (name,),
                    )
            overwritten += 1
        else:
            inserted += 1

        with conn:
            with conn.cursor() as cur:
                cur.execute("CALL upsert_contact(%s, %s, %s::DATE)", (name, email, birthday))
                cur.execute("CALL move_to_group(%s, %s)", (name, group))
                for ph in phones:
                    pnum  = ph.get("phone", "").strip()
                    ptype = ph.get("type", "mobile")
                    if pnum:
                        cur.execute("CALL add_phone(%s, %s, %s)", (name, pnum, ptype))

    print(f"\nDone: {inserted} inserted, {overwritten} overwritten, {skipped} skipped.")
    pause()


def import_csv(conn):
    clear()
    print("── Import from CSV ──")
    filename = input("Filename [contacts.csv]: ").strip() or "contacts.csv"

    try:
        f = open(filename, newline="", encoding="utf-8")
    except FileNotFoundError:
        print(f"File not found: {filename}")
        pause()
        return

    reader  = csv.DictReader(f)
    # Expected columns: name, phone, phone_type, email, birthday, group
    # Rows for the same name accumulate phones
    contacts_map: dict = {}

    for row in reader:
        name = row.get("name", "").strip()
        if not name:
            continue
        if name not in contacts_map:
            contacts_map[name] = {
                "email":    row.get("email", "").strip() or None,
                "birthday": row.get("birthday", "").strip() or None,
                "group":    row.get("group", "").strip() or "Other",
                "phones":   [],
            }
        phone = row.get("phone", "").strip()
        ptype = row.get("phone_type", "mobile").strip() or "mobile"
        if phone:
            contacts_map[name]["phones"].append({"phone": phone, "type": ptype})
    f.close()

    inserted = skipped = 0
    for name, info in contacts_map.items():
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
            exists = cur.fetchone()

        if exists:
            print(f'  Skipping duplicate: "{name}"')
            skipped += 1
            continue

        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    "CALL upsert_contact(%s, %s, %s::DATE)",
                    (name, info["email"], info["birthday"]),
                )
                cur.execute("CALL move_to_group(%s, %s)", (name, info["group"]))
                for ph in info["phones"]:
                    cur.execute("CALL add_phone(%s, %s, %s)", (name, ph["phone"], ph["type"]))
        inserted += 1

    print(f"\nDone: {inserted} inserted, {skipped} skipped.")
    pause()


# ─────────────────────────────────────────────────────────────────────────────
# Main menu
# ─────────────────────────────────────────────────────────────────────────────

MENU = """
╔══════════════════════════════════════╗
║         PhoneBook  –  TSIS 1         ║
╠══════════════════════════════════════╣
║  1.  View all (paginated)            ║
║  2.  Add contact                     ║
║  3.  Delete contact                  ║
║  4.  Add phone to contact            ║
║  5.  Move contact to group           ║
║──────────────────────────────────────║
║  6.  Search (name / email / phone)   ║
║  7.  Filter by group                 ║
║  8.  Search by email                 ║
║  9.  Sort contacts                   ║
║──────────────────────────────────────║
║  10. Export to JSON                  ║
║  11. Import from JSON                ║
║  12. Import from CSV                 ║
║──────────────────────────────────────║
║  0.  Exit                            ║
╚══════════════════════════════════════╝
"""

HANDLERS = {
    "1":  view_all,
    "2":  add_contact,
    "3":  delete_contact,
    "4":  add_phone_menu,
    "5":  move_group_menu,
    "6":  search_menu,
    "7":  filter_by_group,
    "8":  search_by_email,
    "9":  sort_contacts,
    "10": export_json,
    "11": import_json,
    "12": import_csv,
}


def main():
    try:
        conn = get_connection()
    except psycopg2.OperationalError as e:
        print(f"Cannot connect to database:\n{e}")
        sys.exit(1)

    print("Connected to PostgreSQL ✓")

    while True:
        print(MENU)
        choice = input("Choose: ").strip()

        if choice == "0":
            print("Bye!")
            conn.close()
            break

        handler = HANDLERS.get(choice)
        if handler:
            handler(conn)
        else:
            print("Unknown option.")


if __name__ == "__main__":
    main() 