try:
    f = float(input("請輸入華氏溫度:"))
except:
    print("輸入錯誤!")
else:
    C = (f - 32) * 5 / 9
    print(f"華氏溫度{f}F等於攝氏溫度{C}C")
