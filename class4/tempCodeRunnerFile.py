score = int(input("請輸入分數:"))
if score == 100:
    print("滿分保送")
elif score >= 90 and score <= 99:
    print("A")
elif score >= 80 and score < 89:
    print("B")
elif score >= 70 and score < 79:
    print("C")
elif score >= 60 and score < 69:
    print("D")
elif score <= 59 and score > 0:
    print("E")
else:
    print("請重新輸入分數")
