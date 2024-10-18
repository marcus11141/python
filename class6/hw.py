import time


print("開始計時")
time.sleep(5)
print("結束計時")


import turtle as t

t.speed(0)  # 設定畫筆速度為
t.penup()  # 提筆,這樣就不會畫線但是可以移動

for j in range(60):
    for i in range(12):
        t.forward(100)  # 向前移動100個單位
        t.stamp()  # 蓋一個印章
        t.backward(100)  # 向後移動100個單位
        t.right(30)  # 向右移動30度

    t.right(6)  # 轉6度
    t.pendown()  # 下筆
    t.forward(80)  # 向前移動80 ，  秒針出來了
    t.penup()  # 提筆
    time.sleep(1)  # 暫停1秒
    t.backward(80)  # 向後移動80 ，  秒針消失了
    t.clear()  # 清除畫布

t.done()  # 讓視窗不會關閉
