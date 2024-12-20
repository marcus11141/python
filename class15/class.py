# 函式(function) - 就像是一個神奇的工具箱，裡面可以放入我們常常需要使用的指令


# 建立最基本的函式 - 函式名稱後面一定要加上想誇號()，並且記的加上冒號:
def say_hello():
    print("Hello! I am C.S.Lin!")
    print("Nice to meet you!")


say_hello()  # 呼叫函式


# 函式可以接收資料(參數) - 參數就像是函式的原料，可以放入不同的植來得到不同的結果
def say_hello_with_name(name):
    print(f"Hello!{name}!")
    print("Nice to meet you!")


say_hello_with_name("C.S.Lin")


# 函式可以有預設值 - 如果不給參數值，就會使用預設的值，就像是媽媽煮飯時會準備備用食材
def say_hello_with_default(name="C.S.Lin"):
    print(f"Hello!{name}!")
    print("Nice to meet you!")


say_hello_with_default()  # 使用預設值
say_hello_with_default("C.S.Lin")  # 使用新的值

# 區域變數與全域變數 - 想像一下學校和家裡的玩具
# 全域變數 - 就像是學校的遊樂設施，大家都能使用
# 區域變數就像是你書包裡的鉛筆盒，只有你可以使用
toy_name = "玩具熊"  # 全域變數，就像是教室後面的玩具櫃，大家可以拿來玩


def play_with_toy():
    toy_name = "慧魚積木"  # 區域變數，就像是自己帶來的玩具，只有在下課能玩
    print(f"下課時間我在玩{toy_name}")


def share_toy():
    global toy_name  # 告訴Pythoon我要使用大家的玩具
    toy_name = "積木"  # 修改全班共用的玩具
    print(f"大家憶起玩{toy_name}")
