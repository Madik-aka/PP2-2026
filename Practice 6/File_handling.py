import shutil # копирование и перемещение файлов 
import os  #работа с папками и файлами 

# 1.Creation and recording file
with open("sample.txt", "w") as f:
    f.write("Hello, this is sample data\n")
    f.write("Second line\n")

# 2. Read a file
with open("sample.txt", "r") as f:
    print(f.read())

# 3. Append a new line 
with open("sample.txt", "a") as f:
    f.write("Appended line\n")

# Check our changes
with open("sample.txt", "r") as f:
    print(f.read())

# 4. Copy file
shutil.copy("sample.txt", "backup.txt")

# 5. Remove copy
if os.path.exists("backup.txt"):
    os.remove("backup.txt")
    print("backup.txt is deleted")