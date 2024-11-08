# for else
# 如果for迴圈正常結束，則執行else區塊
for i in range(5):
    print(i)
else:
    print("迴圈正常結束")

i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("迴圈正常結束")
    """
使用 for 迴圈建立倒數計時器（以秒為單位）。
- 使用者可以輸入秒數。
- 當倒數計時達到0時，顯示“時間到了！”

範例（在終端機中）：
---
請輸入秒數：3  
3  
2  
1  
時間到了！ 

---

這樣，程式將​​倒數計時並在螢幕上顯示每一秒，直到達到零。
"""
import time

clock = int(input("請輸入秒數："))
while clock > 0:
    print(clock)
    clock -= 1
    time.sleep(1)
else:
    print("時間到了！")
# 可以跳過一次迴圈，繼續執行下一次迴圈
for i in range(5):
    if i == 3:
        continue
    print(i)


i = 0
while i < 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
"""
請輸入您想要跳繩的次數。
學生在跳繩，當他們達到 10 的倍數（如 10、20、30…）時，他們會休息一下。當第 10 次、20 次、30 次…時使用 continue 跳過跳躍。

例子：
請輸入您想跳繩的次數：15
跳1次
跳2次
跳3次
跳4次
跳5次
跳6次
跳7次
跳8次
跳9次
休息一下
跳11次
跳12次
跳13次
跳14次
跳15次
"""
# 輸入想要跳繩的次數
num_of_jumps = int(input("請輸入跳繩的次數: "))
# 開始計算跳繩次數
for i in range(1, num_of_jumps + 1):
    # 如果次數是 10 的倍數，則休息
    if i % 10 == 0:
        print("Take a break")
        continue
    # 其他次數則顯示跳繩次數
    if i == 1:
        print(f"Jump {i} time")
    else:
        print(f"Jump {i} times")

# loop break
# 可以直接結束迴圈，但要注意這個break只會結束所屬迴圈
for i in range(5):
    for j in range(5):
        if j == 3:
            break
        print(j)
    if i == 3:
        break
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    print(i)
    i += 1
