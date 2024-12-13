D = {}

while True:
    print(f"{D}")
    print("1.新增科目成績")
    print("2.刪除科目成績")
    print("3.提交所有成績並顯示平均")
    choice = input("請選擇功能(1-3): ")
    if choice == "1":
        key = input("請輸入科目名稱: ")
        value = int(input("請輸入成績: "))
        D({key: value})
    elif choice == "2":
        key = input("請輸入科目名稱: ")
        D.pop(key)
        if key not in D:
            print("沒有該科目")
    elif choice == "3":
        total = 0
        for i in D:
            total += D
        print(f"平均成績: {total / D}")
        break
