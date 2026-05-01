-- ============================================================
-- PhoneBook  –  TSIS 1  –  Stored Procedures & Functions
-- Run after schema.sql:
--   psql -U postgres -d phonebook -f procedures.sql
-- ============================================================

-- ── From Practice 8 (kept for reference, NOT re-implemented) ─────────────
-- upsert_contact, bulk_insert_contacts, search_contacts (old),
-- paginate_contacts, delete_contact_by_name, delete_contact_by_phone
-- ─────────────────────────────────────────────────────────────────────────


-- ── Practice 8 baseline procedures (required base) ───────────────────────

-- Upsert: insert contact or update email/birthday if name exists
CREATE OR REPLACE PROCEDURE upsert_contact(  -- Update + Insert   если контакта с таким именем нет, то создаем его
    p_name     VARCHAR,                      -- если есть до обновляем его email, дату рождения
    p_email    VARCHAR DEFAULT NULL,
    p_birthday DATE    DEFAULT NULL
)
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO contacts (name, email, birthday)
    VALUES (p_name, p_email, p_birthday)
    ON CONFLICT (name) DO UPDATE
        SET email    = COALESCE(EXCLUDED.email,    contacts.email),       -- using COALESCE 
            birthday = COALESCE(EXCLUDED.birthday, contacts.birthday);
END;
$$;


-- Paginate contacts (name + first phone)
CREATE OR REPLACE FUNCTION paginate_contacts(   -- allows you to output contacts in parts(частями)
    p_limit  INT DEFAULT 10,
    p_offset INT DEFAULT 0
)
RETURNS TABLE (
    contact_name VARCHAR,
    email        VARCHAR,
    birthday     DATE,
    group_name   VARCHAR,
    phones_list  TEXT
)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.name,
        c.email,
        c.birthday,
        g.name          AS group_name,
        STRING_AGG(p.phone || ' (' || COALESCE(p.type,'?') || ')', ', ')   -- we use comand STRING_AGG for to assemble all a person's phones into one beautiful string like "8777 (mobile), 2233 (home)
                        AS phones_list
    FROM contacts c
    LEFT JOIN groups g ON g.id = c.group_id
    LEFT JOIN phones p ON p.contact_id = c.id
    GROUP BY c.name, c.email, c.birthday, g.name, c.created_at
    ORDER BY c.name
    LIMIT  p_limit
    OFFSET p_offset;
END;
$$;


-- Delete contact by username
CREATE OR REPLACE PROCEDURE delete_contact_by_name(p_name VARCHAR)   -- simple deleting form. one by name 
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts WHERE name = p_name;
END;
$$;


-- Delete contact by phone number
CREATE OR REPLACE PROCEDURE delete_contact_by_phone(p_phone VARCHAR)   --one by searching his contacts and delete it
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE id IN (SELECT contact_id FROM phones WHERE phone = p_phone);
END;
$$;


-- ── NEW  –  TSIS 1 procedures ─────────────────────────────────────────────

-- 1. add_phone: add a phone number to an existing contact
CREATE OR REPLACE PROCEDURE add_phone(  --процедура add_phone позволяет добавлять номер в таблицу phones для конкретного человека 
    p_contact_name VARCHAR,
    p_phone        VARCHAR,
    p_type         VARCHAR DEFAULT 'mobile'   
)
LANGUAGE plpgsql AS $$
DECLARE
    v_id INTEGER;
BEGIN
    SELECT id INTO v_id FROM contacts WHERE name = p_contact_name;    --checking if  this contact we hane or not. If not then ouput will be
    IF v_id IS NULL THEN
        RAISE EXCEPTION 'Contact "%" not found', p_contact_name;     --like this 
    END IF;

    IF p_type NOT IN ('home', 'work', 'mobile') THEN
        RAISE EXCEPTION 'Invalid phone type "%". Use: home, work, mobile', p_type;  -- check type of number: home, work, mobile. Workkk is inncorect 
    END IF;

    INSERT INTO phones (contact_id, phone, type)
    VALUES (v_id, p_phone, p_type);
END;
$$;


-- 2. move_to_group: move a contact to a group (creates group if absent)
CREATE OR REPLACE PROCEDURE move_to_group(    -- move contact for example from work to home
    p_contact_name VARCHAR,
    p_group_name   VARCHAR   
)
LANGUAGE plpgsql AS $$
DECLARE
    v_contact_id INTEGER;
    v_group_id   INTEGER;
BEGIN
    -- Find contact
    SELECT id INTO v_contact_id FROM contacts WHERE name = p_contact_name;
    IF v_contact_id IS NULL THEN
        RAISE EXCEPTION 'Contact "%" not found', p_contact_name;
    END IF;

    -- Find or create group
    SELECT id INTO v_group_id FROM groups WHERE name = p_group_name;
    IF v_group_id IS NULL THEN
        INSERT INTO groups (name) VALUES (p_group_name) RETURNING id INTO v_group_id;  -- if a group that we want to join this contact are not created, then programm will insert it
        RAISE NOTICE 'Group "%" created.', p_group_name;
    END IF;

    UPDATE contacts SET group_id = v_group_id WHERE id = v_contact_id;
END;
$$;


-- 3. search_contacts: search by name, email, AND all phones
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE (
    contact_name VARCHAR,
    email        VARCHAR,
    birthday     DATE,
    group_name   VARCHAR,
    phones_list  TEXT
)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT
        c.name,
        c.email,
        c.birthday,
        g.name AS group_name,
        (
            SELECT STRING_AGG(p2.phone || ' (' || COALESCE(p2.type,'?') || ')', ', ')
            FROM phones p2
            WHERE p2.contact_id = c.id
        ) AS phones_list
    FROM contacts c
    LEFT JOIN groups g ON g.id = c.group_id
    LEFT JOIN phones p ON p.contact_id = c.id
    WHERE
        c.name  ILIKE '%' || p_query || '%'
     OR c.email ILIKE '%' || p_query || '%'
     OR p.phone ILIKE '%' || p_query || '%'   -- using ILIKE, for searching and find contact if we write ivan, case sensitive 
    ORDER BY c.name;
END;
$$;