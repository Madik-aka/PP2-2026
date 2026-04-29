import json
import csv
from connect import connect

# --- 1. Пагинация (Просмотр контактов) ---
def show_contacts_paginated():
    limit = 5
    offset = 0
    while True:
        conn = connect()
        if not conn: break
        cur = conn.cursor()
        
        # Исправленный запрос с правильными палочками || для склеивания строк
        query = """
            SELECT first_name || ' ' || last_name as full_name, email 
            FROM contacts 
            ORDER BY first_name 
            LIMIT %s OFFSET %s
        """
        try:
            cur.execute(query, (limit, offset))
            rows = cur.fetchall()
            
            print(f"\n--- Страница {(offset//limit)+1} ---")
            if not rows:
                print("Контов больше нет или база пуста.")
            else:
                for r in rows:
                    print(f"Имя: {r[0]:<25} | Email: {r[1]}")
            
            print("\n[n] Вперед | [p] Назад | [q] В меню")
            cmd = input("Выберите действие: ").lower()
            
            if cmd == 'n' and len(rows) == limit:
                offset += limit
            elif cmd == 'p' and offset > 0:
                offset -= limit
            elif cmd == 'q':
                break
        except Exception as e:
            print(f"Ошибка базы данных: {e}")
            break
        finally:
            cur.close()
            conn.close()

# --- 2. Добавление телефона через процедуру ---
def add_phone_ui():
    print("\n--- Добавление телефона (Процедура) ---")
    first_name = input("Имя контакта: ")
    phone = input("Номер телефона: ")
    p_type = input("Тип (mobile/work/home): ")
    
    conn = connect()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute("CALL add_phone(%s, %s, %s)", (first_name, phone, p_type))
            conn.commit()
            print("Телефон успешно добавлен через процедуру!")
        except Exception as e:
            print(f"Ошибка при вызове процедуры: {e}")
        finally:
            cur.close()
            conn.close()

# --- 3. Экспорт в JSON ---
def export_to_json(filename="contacts.json"):
    conn = connect()
    if not conn: return
    cur = conn.cursor()
    
    query = "SELECT first_name, last_name, email FROM contacts"
    cur.execute(query)
    rows = cur.fetchall()
    
    data = []
    for r in rows:
        data.append({"first_name": r[0], "last_name": r[1], "email": r[2]})
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"Данные успешно экспортированы в {filename}")
    cur.close()
    conn.close()

# --- 4. Импорт из CSV (Тот самый файл conracts.csv) ---
def import_from_csv(filename="conracts.csv"):
    conn = connect()
    if not conn: return
    cur = conn.cursor()
    
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cur.execute("""
                    INSERT INTO contacts (first_name, last_name, email)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (email) DO NOTHING
                """, (row['first_name'], row['last_name'], row['email']))
        conn.commit()
        print(f"Импорт из {filename} завершен!")
    except Exception as e:
        print(f"Ошибка импорта: {e}")
    finally:
        cur.close()
        conn.close()

# --- Главное меню ---
def main():
    while True:
        print("\n" + "="*30)
        print("   PHONEBOOK CONTROL PANEL")
        print("="*30)
        print("1. Список контактов (Пагинация)")
        print("2. Добавить телефон (Процедура)")
        print("3. Экспорт в JSON")
        print("4. Импорт из conracts.csv")
        print("0. Выход")
        print("-" * 30)
        
        choice = input("Выберите пункт: ")
        
        if choice == '1':
            show_contacts_paginated()
        elif choice == '2':
            add_phone_ui()
        elif choice == '3':
            export_to_json()
        elif choice == '4':
            import_from_csv()
        elif choice == '0':
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()