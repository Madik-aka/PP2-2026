import psycopg2
from config import host, user, password, db_name

def main():
    try:
        connection = psycopg2.connect(host=host, user=user, password=password, database=db_name)
        connection.autocommit = True
        cursor = connection.cursor()

        while True:
            action = input("\nChoose action: add/update, search, delete, view, quit\n> ").lower().strip()
            if action == "add" or action == "update":
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                
                # 1. Очищение старых уведомлений
                connection.notices = [] 
                
                # 2. Вызов процедуры
                cursor.execute("CALL public.upsert_contact(%s::varchar, %s::varchar)", (name, phone))
                
                # 3. номер < 11 символов
                is_error = False
                if connection.notices:
                    for notice in connection.notices:
                        if "VALIDATION_ERROR" in notice:
                            print(f"[!] Ошибка базы: {notice.strip()}")
                            is_error = True
                
                # 4. Пишем об успехе только если база не ругалась
                if not is_error:
                    print(f"Contact {name} added/updated successfully.")

            elif action == "search":
                pattern = input("Enter part of name or phone: ")
                # ИЩЕМ НОМЕР
                cursor.execute("SELECT * FROM public.get_contacts_by_pattern(%s::text)", (pattern,))
                rows = cursor.fetchall()
                for row in rows:
                    print(f"Found: {row[0]} - {row[1]}")

            elif action == "delete":
                target = input("Enter name or phone to delete: ")
                # УДАЛЯЕМ
                cursor.execute("CALL public.delete_contact(%s::varchar)", (target,))
                print(f"Contact {target} removed.")

            elif action == "view":
                print("\nLast 10 added contacts:")
                # Вызов функции с лимитом 10 
                cursor.execute("SELECT * FROM public.get_contacts_paginated(10, 0)")
                rows = cursor.fetchall()
                if not rows:
                    print("No contacts found.")
                for row in rows:
                    print(f"{row[0]}: {row[1]}")

            elif action == "quit":
                break
            else:
                print("Invalid action.")

    except Exception as _ex:
        print("[INFO] Error:", _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("[INFO] Connection closed.")

if __name__ == "__main__":
    main()