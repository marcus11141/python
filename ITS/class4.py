# "".format() 可以用來格式化字串
# "{1:s} {0:s}".format("hello", "world")  # world hello
# :的左邊是放入的變數的index, 右邊是格式化的型態設定


# 另一種格式化的方式是在字串當中放入 %?
# %s 可以用來格式化字串
# example: print("hello %s" % "world") # hello world
# %d 可以用來格式化整數
# example: print("hello %d" % 1) # hello 1
# %f 可以用來格式化浮點數
# example: print("hello %f" % 1.0) # hello 1.000000
# 再%跟型態符號中間可以放入數字來設定格式化的寬度
# %5d 可以用來格式化整數到5位數 1=>    1
# example: print("hello %5d" % 1) # hello    1
# %05d 可以用來格式化整數到5位數 1=> 00001
# example: print("hello %05d" % 1) # hello 00001
# %5.2f 可以用來格式化浮點數到5位數 1=>  1.00
# example: print("hello %5.2f" % 1.0) # hello  1.00
# %05.2f 可以用來格式化浮點數到5位數 1=> 01.00
# example: print("hello %05.2f" % 1.0) # hello 01.00
# %-5s 可以用來格式化字串到5位數，靠左對齊 'a' => 'a    '
# example: print("hello %-5s" % "a") # hello a
# %5s 可以用來格式化字串到5位數，靠右對齊 'a' => '    a'
# example: print("hello %5s" % "a") # hello     a
# %.3s 可以用來限制字串最大長度為3 'hello' => 'hel'
# example: print("hello %.3s" % "hello") # hello hel
# %10.3s 可以用來格式化字串到10位數，且最大長度為3 'hello' => '       hel'
# example: print("hello %10.3s" % "hello") # hello        hel
# 函式 (Function) - 就像是一個神奇的工具箱，裡面可以放入我們常常需要使用的指令
# 建立最基本的函式 - 函式名稱後面一定要加上小括號()，並且記得加上冒號:
def say_hello():
    print("Hello! I am Ming!")
    print("Nice to meet you!")


say_hello()  # 呼叫函式


# 函式可以接收資料 (參數) - 參數就像是函式的原料，可以放入不同的值來得到不同的結果
def say_hello_with_name(name):
    print(f"Hello! {name}!")
    print("Nice to meet you!")


say_hello_with_name("Hua")


# 函式可以有預設值 - 如果不給參數值，就會使用預設的值，就像是媽媽煮飯時會準備備用食材
def say_hello_with_default(name="Ming"):
    print(f"Hello! {name}!")
    print("Nice to meet you!")


say_hello_with_default()  # 使用預設值
say_hello_with_default("Mei")  # 使用新的值

# 區域變數與全域變數 - 想像一下學校和家裡的玩具
# 全域變數就像是學校的遊樂設施，每個人都可以使用
# 區域變數就像是你書包裡的鉛筆盒，只有你自己可以用
toy_name = "玩具熊"  # 全域變數，就像是教室後面的玩具櫃，大家都可以拿來玩


def play_with_toy():
    toy_name = "慧魚積木"  # 區域變數，就像是自己帶來的玩具，只能在下課時間玩
    print(f"下課時間我在玩：{toy_name}")  # 顯示：慧魚積木


def share_toy():
    global toy_name  # 告訴Python我要使用大家的玩具
    toy_name = "積木"  # 修改全班共用的玩具
    print(f"大家一起玩：{toy_name}")


# 讓我們來看看玩具的變化：
print(f"一開始教室的玩具是：{toy_name}")  # 顯示：玩具熊
play_with_toy()  # 下課時間我在玩：慧魚積木
print(f"下課後教室的玩具還是：{toy_name}")  # 顯示：玩具熊（沒有改變）

print("\n現在讓我們改變大家的玩具：")
print(f"教室的玩具是：{toy_name}")  # 顯示：玩具熊
share_toy()  # 大家一起玩：積木
print(f"現在教室的玩具變成：{toy_name}")  # 顯示：積木（真的改變了）


# 函式可以回傳資料 - 就像是我們請人幫忙買東西，他會把東西帶回來給我們
# return 是回傳的關鍵字，代表這個函式處理完後要交回什麼結果
def calculate_sum(number1, number2=0):
    total = number1 + number2
    return total


result = calculate_sum(5, 3)
print(f"Sum of 5+3 is: {result}")
result = calculate_sum(10)  # 使用預設值0
print(f"Sum of 10+0 is: {result}")


# 函式回傳值的示範 - 就像是我們給媽媽錢買東西，媽媽買完會把找的錢還給我們
def pocket_money(money):
    # 假設買一個麵包要30元
    bread_price = 30
    change = money - bread_price
    print(f"買完麵包後，還剩下 {change} 元")
    return change


money_left = pocket_money(50)
print(f"媽媽把剩下的 {money_left} 元還給我")


# 函式參數預設值的順序 - 有預設值的參數一定要放在沒有預設值的參數後面
# 就像是排隊買餐點，一定要先點主餐，才能選擇要不要加購配菜
# 這樣是對的 :
def order_lunch(main_dish, side_dish="薯條"):
    print(f"主餐是：{main_dish}")
    print(f"配菜是：{side_dish}")


order_lunch("漢堡")  # 只點主餐
order_lunch("漢堡", "沙拉")  # 主餐和配菜都點

# 這樣是錯的:
# def wrong_order(dessert="冰淇淋", meal):  # 會出錯！
#     print(f"飯是：{meal}")
#     print(f"甜點是：{dessert}")
