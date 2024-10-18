"""
作業說明:
讓turtle蓋出一個時鐘數字的位置
總共會蓋出12個印章
"""

import turtle as t

t.penup()  # 提筆, 這樣就不會畫線但是可以移動

for i in range(12):
    t.forward(100)  # 向前移動100個單位
    t.stamp()  # 蓋一個印章
    t.backward(100)  # 向後移動100個單位
    t.right(30)  # 向右移動30度


t.done()  # 讓視窗不會關閉
