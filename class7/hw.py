"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
3,7的倍數顯示在螢幕上, 其餘不顯示
hint:可以使用%取餘數進行判斷
EX
請輸入正整數:20
3
6
7
9
12
14
15
18
請輸入要印出的箭頭大小
hint:
可利用字串乘法
>>>val="*" * 3
>>>print(val)
>>>***
EX:
請輸入要印出的箭頭大小:3
  *  
 *** 
*****
  *  
  *  
  * 
"""

num = int(input("請輸入正整數:"))
i = 1
while i <= num:
    if i % 3 == 0 or i % 7 == 0:
        print(i)
    i += 1

arrow_size = int(input("請輸入要印出的箭頭大小: "))
for i in range(arrow_size):
    spaces = " " * (arrow_size - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
for i in range(arrow_size):
    spaces = " " * (arrow_size - 1)
    print(spaces + "*")
