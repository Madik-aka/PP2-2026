import os
import shutil

# 1. Создание папки и внутри него еще одну папку 
os.makedirs("folder/subfolder", exist_ok=True)
print("Созданы папки folder/subfolder")

# 2. Список файлов и папок текущей директории
print("Список файлов и папок в текущей директории Practice 6:")
print(os.listdir("."))    #Точка . — это сокращение для «текущая папка».

# 3. Поиск файлов с окончание .txt
print("Файлы c расширением .txt:")
for file in os.listdir("."):
    if file.endswith(".txt"):
        print(file)

# 4. Перемещение и копирование файлов в папку 
shutil.move("sample.txt", "folder/sample.txt")
print("sample.txt перемещён в folder/sample.txt")
shutil.copy("folder/sample.txt", "folder/copy.txt")
print("Сделана копия folder/sample.txt -> folder/copy.txt")