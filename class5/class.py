# 取餘數
# print(3 % 2)
try:
    f = int(input("請輸入數字:"))
except:
    print("輸入錯誤!")
else:
    if f % 2 == 0:
        print(f"數字{f}是偶數")
    else:
        print(f"數字{f}是奇數")

# 匯入模組
# import turtle # 匯入模組turtle
import turtle as t  # 匯入模組turtle的別名t

# from import turtle * # 匯入模組turtle的所有指令
# from import turtle done # 匯入模組turtle的當中done指令

# done()
# turtle.done()
t.speed(1)  # 設定速度為1
t.forward(100)  # 向前移動100個單位
t.backward(100)  # 向後移動200個單位
t.left(90)  # 向左移動90度
t.forward(100)  # 向前移動100個單位
t.right(90)  # 向右移動90度
t.forward(100)  # 向前移動100個單位
t.right(90)  # 向右移動90度
t.forward(100)  # 向前移動100個單位
# t.right(90)  # 向右移動90度
# t.forward(50)  # 向前移動50個單位
# t.right(90)  # 向右移動90度
# t.forward(100)  # 向前移動50個單位
# t.right(180)  # 向右移動90度
# t.forward(50)  # 向前移動50個單位
# t.right(90)  # 向右移動90度
# t.forward(50)  # 向前移動50個單位
# t.right(180)  # 向右移動90度
# t.forward(100)  # 向前移動100個單位
# 發現turtle一開始面向右邊
t.done()  # 讓視窗不會關閉

# for example
# for的組成有三個部份
# for 迴圈變數 in 範圍
# 迴圈變數只能活在for迴圈裡面
# 迴圈變數每回合都會範圍中取出一個值
for i in range(6):  # range 可以產生一組數字, 0~5
    print(i)

for i in range(1, 6):  # 1~5
    print(i)

for i in range(1, 6, 2):  # 1,3,5
    print(i)

import turtle as t

t.penup()  # 提筆ㄝ這樣就不會畫線但是可以移動
t.forward(100)  # 向前移動100個單位
t.stamp()  # 蓋一個印章
t.done()  # 讓視窗不會關閉
