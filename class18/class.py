# 檔案讀寫
# 判斷檔案是否存在 - 使用 os.path.ex.ists()函式
import os

# 相對路徑代表相對於目前的工作目錄的路徑
# 絕對路徑代表完整的路徑
if os.path.exists("class17/hw.py"):
    # C:\Users\ocato\OneDrive\桌面\python\class18\class.py
    print("檔案存在!")
else:
    print("檔案不存在!")

# open()開啟模式
# r - 讀取模式、檔案必須存在
# w - 寫入模式、檔案不存在會自動建立
# a - 附加模式、檔案不存在會自動建立
# r+ - 讀取與寫入模式、檔案必須存在
# w+ - 讀取與寫入模式、檔案不存在會自動建立
# a+ - 讀取與附加模式、檔案不存在會自動建立
# 讀取檔案 - 使用open()函式
# 例如(For example:)
file = open("class18/file test.py", "r")
print(file.read())
file.close()

# 讀取檔案 - 使用with open() as
# 例如(For example:)
with open("class18/file test.py", "r") as file:
    print(file.read())

# 寫入檔案 - 使用open()函式
# 例如(For example:)
file = open("class18/file test.py", "w")
file.write("print(Hello world!')")
file.close()
