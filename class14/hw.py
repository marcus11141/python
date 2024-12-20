score_dict = {}
while True:
    for subject, score in score_dict.items():
        print(f"{subject}: {score}")
    print("1. 新增科目成績")
    print("2. 刪除科目成績")
    print("3. 提交所有成績並顯示平均")
    choice = input("請輸入功能編號: ")
    print("==========================")
    
    if choice == "1":
        subject = input("請輸入科目: ")
        if subject in score_dict:
            print("科目已存在")
        else:
            while True:
                try:
                    score = int(input("請輸入成績: "))
                    score_dict[subject] = score
                    break
                except:
                    print("請重新輸入數字")
    elif choice == "2":
        subject = input("請輸入想刪除的科目: ")
        if subject in score_dict:
            score_dict.pop[subject]
            print("刪除成功")
        else
            print("科目不存在")
    elif choice == "3":
        if len(score_dict) == 0:
            print("沒有成績")
        else:
            total_score = 0
            for subject, score in score_dict.items():
                print(f"{subject}: {score}")
            print(f"平均為:{sum(score_dict.values()) / len(score_dict)}")
            break
    else:
        print("你特麼玩我呢?")

    print("==========================")s