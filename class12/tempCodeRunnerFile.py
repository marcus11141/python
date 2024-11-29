order = []
while True:
    print(order)
    print("1.新增餐點")
    print("2. 刪除餐點")
    print("3. 提交菜單")
    i = int(input("請選擇功能:"))
    if i == 1:
        print("請輸入餐點名稱:")
        name = input()
        print("請輸入餐點數量:")
        num = int(input())
        order.append([name, num])
    elif i == 2:
        print("請輸入要刪除的餐點名稱:")
        name = input()
        for i in range(len(order)):
            if order[i][0] == name:
                order.pop(i)
                break
    elif i == 3:
        print("漢堡:", order[0][1])
        print("薯條:", order[1][1])
        print("可樂:", order[2][1])
        break