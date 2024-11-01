# price = int(input("請輸入商品的價格: "))
# sum = 0
# while price != 0:
#     sum += price
#     print(f"目前總金額是 {sum}")
#     price = int(input("請輸入商品的價格: "))
prime = int(input("請輸入數字: "))
is_prime = True
for i in range(2, prime):
    if prime % i == 0:
        is_prime = False

if is_prime and prime > 1:
    print(f"{prime}是質數")
else:
    print(f"{prime}不是質數")
