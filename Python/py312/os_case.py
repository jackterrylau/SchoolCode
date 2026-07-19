# coding=utf-8

"""
## os module
==os module is for operation system dir/file management==
### Directory Management
1. os.mkdir(path_for_dir): create a directory
2. os.rmdir(path_for_dir): remove a directory
3. os.listdir(path_for_dir): list the sub-directory and files under a directory
4. os.curdir: list current directory
5. os.path.dirname(path): return the directory name of a path
6. os.path.abspath(path): return the completed path
7. os.path.isdir(path): check a path if is to a directory

### Files Management
1. os.remove(path_to_file): remove a file
2. os.path.getsize(path_to_file): return the file size by bytes
3. os.path.basename(path): return the directory/file of a path
4. os.path.isfile(path): check a path if is to a file
5. os.path.exists(path_to_file): check a file if is existed
"""

import os

houses_price_file_name = "data/台北房價資料.txt"

if not os.path.exists(houses_price_file_name):
    if not os.path.exists("data"): os.mkdir("data")
    with open(houses_price_file_name, 'w+', encoding="utf-8") as houses_price_file:
        houses_price_file.write("台北房價資料 TXT")

print("- houses_price_file_name abs path:", os.path.abspath(houses_price_file_name))
print("- houses_price_file_name base name:", os.path.basename(houses_price_file_name))
print("- houses_price_file_name directory name:", os.path.dirname(houses_price_file_name))
print("- houses_price_file({0}) Size:{1} bytes".format(os.path.basename(houses_price_file_name), os.path.getsize(houses_price_file_name)))

