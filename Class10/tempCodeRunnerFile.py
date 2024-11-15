import random as r

num = r.randint(1, 100)

while True:
    num2 = int(input("請輸入1~100:"))
    if num2 > num:
        print("再大一點")
    elif num2 < num:
        print("再小一點")
    else:
        print("猜到了!")
        break
