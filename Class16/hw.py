"""
成績系統改寫作業 Score System Rewrite Assignment
--------------------------------------------

任務說明 (Task Description)：
請把成績系統的每個功能變成一個獨立的功能包，就像把工具分門別類放好一樣！
Please turn each feature of the score system into separate functions, just like organizing tools into different boxes!

需要製作的功能包 (Functions to Create)：
1. 新增功能 (Add Function):
   - def add: 幫我們加入新科目和分數
   - For adding new subject and score

2. 刪除功能 (Delete Function):
   - def delete: 可以刪掉不要的科目和分數
   - For removing subject and score

3. 離開功能 (Exit Function):
   - def exit: 結束程式並算出平均分數
   - For ending program and calculating average

完成方式 (How to Complete)：
- 要像積木一樣，把每個功能都組裝好
- Build each function like blocks
- 保持原本的操作方式不變
- Keep the same way of using the program
"""
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