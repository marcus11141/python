"""
輸入一組整數範圍，將範圍中的所有質數顯示於畫面上。
EX：
請輸入開始整數:10
請輸入結束整數:50
11
13
17
19
23
29
31
37
41
43
47
"""

start = int(input("請輸入開始整數: "))
end = int(input("請輸入結束整數: "))
for prime in range(start, end + 1):

    is_prime = True
    for i in range(2, prime):
        if prime % i == 0:
            is_prime = False

    if is_prime and prime > 1:
        print(f"{prime}是質數")
