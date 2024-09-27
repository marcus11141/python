# 型態轉換
# int() 轉換成整數
# float() 轉換成浮點數
# str() 轉換成字串
# bool() 轉換成布林值
# print("-----------------------")
# print(int("123"))  # 123
# print(int(123.9999))  # 123
# print(int(True))  # 1
# print(int(False))  # 0
# print("-----------------------")
# print(float("123.456"))  # 123.456
# print(float(123))  # 123.0
# print(float(True))  # 1.0
# print(float(False))  # 0.0
# print("-----------------------")
# print(str(123))  # 123
# print(str(123.456))  # 123.456
# print(str(True))  # True
# print(str(False))  # False
# print("-----------------------")
# print(bool(123))  # True
# print(bool(0))  # False
# print(bool(-1))  # True
# print(bool(""))  # False
# print(bool("0"))  # True
# print("-----------------------")
# input() 讓使用者在終端機詩入資料
#  input() 的叧湖內殼以放入"提示字串"
# a = input("請輸入數字:")
#  透過 input() 輸入的資料都是字串
# print(a + "1")  # 字串相加
# print(int(a) + 1)  # 將字串轉換成整數再相加
# print("-----------------------")
# 格式化字串 f-string
# bmi = 17.3
# print(f"你的BMI為{bmi}")
# print("-----------------------")
# L = input("請輸入正方形的邊長:")
# area = int(L) * int(L)
# print(f"正方形面積為{area}")
# print("-----------------------")
# try except 錯誤處理
n = int(input("請輸入數字:"))
try:
    # 嘗試執行可能出錯的程式碼
    n = int(input("請輸入數字:"))

except:
    # 如果錯誤發生，執行這段程式碼
    print("你輸入的不是數字")

else:
    # 如果沒有錯誤發生，執行這段程式碼
    print(n + 1)
