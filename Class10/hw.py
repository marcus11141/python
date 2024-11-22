import random

start = 0
end = 100
m = random.randrange(1, 101)
num = 0
while num != m:
    num = int(input(f"請輸入{start}~{end}數字:"))
    if num < m:
        print("再大一點")
        if num > start:
            start = num
    elif num > m:
        print("再小一點")
        if num < end:
            end = num

print("猜到了!")
