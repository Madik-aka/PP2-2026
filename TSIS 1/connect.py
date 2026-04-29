import psycopg2

def connect():
    try:
        # Вписываем данные прямо сюда, без всяких конфигов
        conn = psycopg2.connect(
            host="localhost",
            database="postgres", # проверь имя базы в pgAdmin
            user="postgres",
            password="1234"      # ТВОЙ ПАРОЛЬ ТУТ
        )
        return conn
    except Exception as error:
        print(f"Ошибка подключения: {error}")
        return None