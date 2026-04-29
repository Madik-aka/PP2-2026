from configparser import ConfigParser
import os

def load_config(filename='database.ini', section='postgresql'):
    # Проверим, существует ли файл вообще
    if not os.path.exists(filename):
        raise Exception(f"Файл {filename} вообще не найден в {os.getcwd()}")

    parser = ConfigParser()
    # Замени старую строку на эту
    parser.read(filename, encoding='utf-8')

    # Выведем в консоль все секции, которые нашел Python
    print(f"Найденные секции в файле: {parser.sections()}")

    if parser.has_section(section):
        params = parser.items(section)
        return {param[0]: param[1] for param in params}
    else:
        raise Exception(f'Секция {section} не найдена. Список секций: {parser.sections()}') 