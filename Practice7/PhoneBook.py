import psycopg2
import csv
import os

# 1. Настройки подключения
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "1234", 
    "host": "localhost",
    "port": "5432"
}

def init_db():
    """Функция для создания таблицы, если её еще нет"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(100) NOT NULL,
                phone_number VARCHAR(20) NOT NULL UNIQUE
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
        print("[System] База данных готова к работе.")
    except Exception as e:
        print(f"[Error] Ошибка при создании таблицы: {e}")
        exit()

def menu():
    init_db()  # проверка таблицы
    
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
    except Exception as e:
        print(f"[Error] Не удалось подключиться к серверу: {e}")
        return

    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Add contact (Console)")
        print("2. Import from CSV (data.csv)")
        print("3. Update contact")
        print("4. Show ALL contacts")
        print("5. Search contact")
        print("6. Delete contact")
        print("0. Exit")

        choice = input("\nChoose an option: ").strip()

        # --- 1. ДОБАВИТЬ ВРУЧНУЮ ---
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            try:
                cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (name, phone))
                conn.commit()
                print("Contact added!")
            except Exception as e:
                conn.rollback()
                print(f"Error: {e}")

       
        #2. ИМПОРТ ИЗ CSV
        elif choice == "2":
            filename = "data.csv"
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if len(row) >= 2: # Проверяем, что в строке есть имя и номер
                            cur.execute(
                                "INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", 
                                (row[0].strip(), row[1].strip())
                            )
                conn.commit()
                print("Data from CSV imported successfully!")
            except Exception as e:
                conn.rollback()
                print(f"Error during import: {e}")

        #3. ОБНОВИТЬ
        elif choice == "3":
            target = input("Enter name of contact to update: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone: ")
            cur.execute(
                "UPDATE phonebook SET first_name=%s, phone_number=%s WHERE first_name=%s",
                (new_name, new_phone, target)
            )
            conn.commit()
            print("Contact updated!")

        #4. ПОКАЗАТЬ ВСЁ
        elif choice == "4":
            cur.execute("SELECT * FROM phonebook ORDER BY id")
            rows = cur.fetchall()
            if rows:
                print("\nID | NAME | PHONE")
                print("-" * 25)
                for row in rows:
                    print(f"{row[0]} | {row[1]} | {row[2]}")
            else:
                print("Phonebook is empty.")

        #5. ПОИСК
        elif choice == "5":
            key = input("Search by name or phone prefix: ")
            cur.execute(
                "SELECT * FROM phonebook WHERE first_name ILIKE %s OR phone_number LIKE %s",
                (f"%{key}%", f"{key}%")
            )
            results = cur.fetchall()
            for r in results:
                print(f"ID: {r[0]} | Name: {r[1]} | Phone: {r[2]}")

        #6. УДАЛИТЬ
        elif choice == "6":
            key = input("Enter name or phone to delete: ")
            cur.execute("DELETE FROM phonebook WHERE first_name=%s OR phone_number=%s", (key, key))
            conn.commit()
            print("Deleted.")

        #0. ВЫХОД
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

    cur.close()
    conn.close()
    print("Goodbye!")

if __name__ == "__main__":
    menu() 