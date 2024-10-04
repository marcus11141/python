# 比較運算子
print(1 == 1)  # True, 1 等於 1
print(1 != 1)  # False, 1 不等於 1
print(1 > 1)  # False, 1 大於 1
print(1 < 1)  # False, 1 小於 1
print(1 >= 1)  # True, 1 大於等於 1
print(1 <= 1)  # True, 1 小於等於 1
print("-----------------------")
# 邏輯運算子
print(True and True)  # True, True和True
print(True and False)  # False, True和False
print(False and False)  # False, False和False
print(True or True)  # True, True和True
print(True or False)  # True, True和False
print(False or False)  # False, False和False
print(not True)  # False, 非True
print(not False)  # True, 非False
print("-----------------------")
# if
pwd = input("請輸入密碼:")
if pwd == "123":  # 如果密碼是123
    print("密碼正確")  # 印出密碼正確

# if else
pwd = input("請輸入密碼:")
if pwd == "123":  # 如果密碼是123
    print("密碼正確")
else:  # 如果密碼不是123
    print("密碼錯誤")  # 印出密碼錯誤

# if elif else
pwd = input("請輸入密碼:")
if pwd == "123":  # 如果密碼是123
    print("歡迎登入Damn")  # 印出歡迎登入Damn
elif pwd == "456":  # 如果密碼是456
    print("歡迎登入Dab")  # 印出歡迎登入Dab
else:
    print("密碼錯誤")

# if elif else是連續的判斷，只要有一個條件成立，後面的判斷就不會執行

# if 一定要有，elif可以有多個但是選用，else只能有一個但是選用
score = int(input("請輸入分數:"))
if score == 100:
    print("滿分保送")
elif score >= 90 and score <= 99:
    print("A")
elif score >= 80 and score < 89:
    print("B")
elif score >= 70 and score < 79:
    print("C")
elif score >= 60 and score < 69:
    print("D")
elif score <= 59 and score > 0:
    print("E")
elif score == 0:
    print("you get out here")
else:
    print("請重新輸入分數")
