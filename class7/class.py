# # # 99乘法表
# # for a in range(1, 10):  # 讓 a 從 1 執行到 9
# #     for b in range(1, 10):  # 讓 b 從 1 執行到 9
# #         print(f"{a}x{b}={a*b}")  # 使用格式化字串，印出產生對應的字串
# # while 迴圈
# # while loop
# # 這是條件式迴圈, 當條件成立時,就會執行回圈內的程式
# i = 1
# while i < 10:
#     # 當i等於10時,就會執行到這行程式
#     print(i)
#     i = i + 1

# # 算術指定運算子
# # +=, -=, *=, /=, %=, **=, //=
# # x = x + 1等於x += 1
# # x = x - 1等於x -= 1
# # x = x * 1等於x *= 1
# # x = x / 1等於x /= 1
# # x = x % 1等於x %= 1
# # x = x ** 1等於x **= 1
# # x = x // 1等於x //= 1
# i = 1
# while i < 10:
#     print(i)
#     i += 1  # 等於 i = i + 1
"""
升級版密碼門
•輸入正確的時候會顯示歡迎文字
•輸入錯誤則會要求重新輸入
•如果一直輸入錯誤可以無限循環輸入直到正確為止
"""

"""
while True:
    p = input("請輸入密碼: ")
    if p == "123456":
        print("歡迎")
        break
    else:
        print("密碼錯誤，請重新輸入")
"""
user_input = " "
while user_input != "1234":
    user_input = input("請輸入密碼: ")
print("歡迎")
