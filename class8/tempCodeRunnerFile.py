prime = int(input("請輸入數字: "))
for i in range(2, prime):
    if prime % i == 0:
        print(f"{prime}不是質數，因為{i}整除{prime}")
    else:
        print(f"{prime}是質數")