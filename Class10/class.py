"""
import random as r  # 這是隨機模組

# random.randrange設定範圍的方式跟range一樣, 特性也不一樣不包含最後一數字
# random.randrange的功能是隨機取得一個數字, range是產生一組數字
print(r.randrange(10))  # 從0~9隨機取得一個數字
print(r.randrange(1, 10))  # 從1~9隨機取得一個數字
print(r.randrange(1, 10, 2))  # 從[1, 3, 5, 7, 9]隨機取得一個數字

# random.randint 設定範圍的方式必須要有開始跟結束, 且包含最後一個數字
# 不能跳數字抽籤
print(r.randint(1, 10))  # 從1~10中隨機取得一個數字
"""

# import random as r

# num = r.randint(1, 100)

# while True:
#     num2 = int(input("請輸入1~100:"))
#     if num2 < num:
#         print("再大一點")
#     elif num2 > num:
#         print("再小一點")
#     else:
#         print("猜到了!")
#         break

# List 清單
# List 可以存入很多資料，每筆資料用` , `隔開
# List 可以存入不同型態的資料
# List 最外層用`[]`包起來
L = [1, 2, 3, 4, 5]  # 數字
print(L)
# 不同型態混合
L = [1, "2", 3, 4, 5, "Hello", ["World", 6]]  # 數字, 字串, List
print(L)

# List 取值
# List 取值方式跟字串一樣, 用`[]`取值
# List 取值方式跟字串一樣, 也可以用`[:]`取值
# List 當中資料的編號(index)以0為開始
L = [1, 2, 3, 4, 5]
print(L[0])  # 取得第一個值
print(L[1])  # 取得第二個值
print(L[2])  # 取得第三個值

# List 取值方式跟字串一樣, 也可以用`[:]`取值
# 設定範圍的方式跟range很像, 不包含最後一個數字
print(L[1:4:2])  # 取得第一個到第四個, 且間隔為2
print(L[0:3])  # 取得第一個到第三個值
print(L[:3])  # 取得第一個到第三個值
print(L[3:])  # 取得第四個到最後一個值
print(L[:])  # 取得全部值
