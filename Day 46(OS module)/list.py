import os

folders = os.listdir("E:\LearnPython")

print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"E:\LearnPython/{folder}"))
