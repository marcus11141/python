"""
點餐機
有一個空的菜單 order = []
1. 新增餐點
example:
    ```
    請輸入餐點名稱: 漢堡
    目前order=['漢堡', '漢堡']
    ```
2. 刪除餐點，移除所有重複的餐點
example:
    輸入2之後會顯示
    ```
    請輸入餐點名稱: 漢堡
    目前order=[]
    ```  
3. 提交菜單，提交的時候要印出每個餐點點了幾份，結束程式
example:
    輸入3之後會顯示
    ```
    漢堡:2
    薯條:1
    可樂:3
    ```
"""

order = []


while True:
    print(f"目前order={order}")
    print("1. 新增餐點")
    print("2. 刪除餐點")
    print("3. 提交菜單")

    choice = input("請選擇功能(1-3): ")
    if choice == "1":
        item = input("請輸入餐點名稱: ")
        order.append(item)
    elif choice == "2":
        item = input("請輸入餐點名稱: ")
        if item in order:
            for x in range(order.count(item)):
                order.remove(item)
    elif choice == "3":
        items = (
            []
        )  # order=["漢堡", "薯條", "可樂", "可樂", "可樂"] -> items=["漢堡", "薯條", "可樂"]
        for x in order:
            if x not in items:
                items.append(x)

        for x in items:
            print(f"{x}:{order.count(x)}")

        break
    else:
        print("請輸入錯誤，請重新輸入")
