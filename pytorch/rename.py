import os

# 获取当前目录下所有子文件夹的名称
folders = [f for f in os.listdir('.') if os.path.isdir(f)]

# 遍历所有子文件夹，将名称中的"chapter04_"替换为"chapter05_"，将名称中的"chapter05_"替换为"chapter06_"，依此类推
for i in range(3, 16):
    current_chapter = "chapter{:02d}_".format(i)
    next_chapter = "chapter{:02d}_".format(i+1)
    
    for folder in folders:
        if folder.startswith(current_chapter):
            new_folder = next_chapter + folder[len(current_chapter):]
            os.rename(folder, new_folder)
            print(f"将文件夹 {folder} 重命名为 {new_folder}")
        else: 
            print("Folder name is %s"%(folder))
