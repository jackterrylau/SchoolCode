# os_case_learn.md
## os module
== os module is for operation system dir/file management ==
### Directory Management
1. `os.mkdir(path_for_dir)`: create a directory
2. `os.rmdir(path_for_dir)`: remove a directory
3. `os.listdir(path_for_dir)`: list the sub-directory and files under a directory
4. `os.curdir`: list current directory
5. `os.path.dirname(path)`: return the directory name of a path
6. `os.path.abspath(path)`: return the completed path
7. `os.path.isdir(path)`: check a path if is to a directory

### Files Management
1. `os.remove(path_to_file)`: remove a file
2. `os.path.getsize(path_to_file)`: return the file size by bytes
3. `os.path.basename(path)`: return the directory/file of a path
4. `os.path.isfile(path)`: check a path if is to a file
5. `os.path.exists(path_to_file)`: check a file if is existed

## Python Tips
- with open(path_to_file, open_mode, encoding="utf-8") as file_name
  - open a file by `with as` resource management statement
   - open() parameters:
     1. open_mode: 開啟檔案的方式(是要讀要寫)
     2. encoding: 檔案編碼方式, 預設是 `utf-8`
   - when use the resource management to open a file, we can ignore `finally`  statement to do `close()` function

Open Mode Parameter

|Open Action|File Type|Sign|Value|Descrtiption|  
|:--------------:|:--------------:|:------------:|:------------:|:--------------:|
|r|NA|NA|r|僅讀取文件(=rt)|
|w|NA|NA|w||僅以覆寫方式開啟已存在文件(=wt)|
|a|NA|NA|a|僅以附加寫入方式開啟已存在文件(=at)|
|r|t|NA|rt|僅讀取文件(=rt)|
|w|t|NA|wt|僅以覆寫方式開啟已存在文件|
|a|t|NA|at|僅以附加寫入方式開啟已存在文件|
|r|NA|+|r+|僅讀取文件,檔案不存在則創建|
|w|NA|+|w+|僅以覆寫方式開啟文件,檔案不存在則創建|
|a|NA|+|a+|僅以附加寫入方式開啟文件,檔案不存在則創建|
|r|b|NA|rt|僅讀取2進制檔案|
|w|b|NA|wt|僅以覆寫方式開啟已存在2進制檔案|
|a|b|NA|at|僅以附加寫入方式開啟已存在2進制檔案|
|r|b|+|r+|僅讀取2進制檔案,檔案不存在則創建|
|w|b|+|w+|僅以覆寫方式開啟2進制檔案,檔案不存在則創建|
|a|b|+|a+|僅以附加寫入方式開啟2進制檔案,檔案不存在則創建|

Code Example:
```Python
try:
    with open("data.txt", w+, encoding="utf-8") as f:
        f.write("Test 'with as' Statement")
except Execption as e:
    print("get an error:", e)
# finally:
#   f.close()
```