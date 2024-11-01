num = int(input("請輸入正整數:"))
i = 1
while i <= num:
    if i % 3 == 0 and i % 7 == 0:
        print(i)
    i += 1
