juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "可樂", "系統關閉", "柳橙汁"]
while True:
    for i in range(len(juices_list)):
        print(f"{i + 1}. {juices_list[i]}")

    try:
        slelect = int(input("請輸入編號:"))
    except:
        print("輸入錯誤，請重新輸入")
        continue
    if slelect > len(juices_list):
        print("輸入錯誤，請重新輸入")
        continue
    elif juices_list[slelect - 1] == "系統關閉":
        print("~~系統關閉~~")
        break

    else:
        print(f"您點的商品是{juices_list[slelect - 1]}")
        break
