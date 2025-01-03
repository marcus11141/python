a = ["a", "b", "c"]
b = a  # 把a的"記憶體位置"指定給b，所以a和b指向同一個"記憶體位置"
b[0] = "d"  # 把b的第一個元素，a也會跟著改變
print(a)  # 顯示:["d", "b", "c"]

a = 10
b = a  # 把a的"值"指定給b，所以a和b的"值"相同
b = 20  # 修改b的值，a不會改變
print(a)  # 顯示:10


# def doc用途
def add(a, b):
    """
    加法函式
    :param a: 數字1
    :param b: 數字2
    :return: a + b
    """
    return a + b


# 使用help 函式可以查看函式的說明
# 例如:(For example:)
help(add)

# 使用.__doc__屬性可以查看函式的說明文件
# 例如:(For example:)
print(add.__doc__)
print(add.__name__)  # 顯示: add 函式的名稱

# eval(input())- 這個函式可以讓使用者輸入的文字變成程式碼執行
# 例如:(For example:)
ans = eval("5+3")
print(ans)  # 顯示:8

# 這樣就可以讓使用者輸入數學運算式，然後計算結果
# 例如:(For example:)
ans = eval(input("請輸入數學運算式:"))
print(ans)
# 例如輸入:(For example, input:)
# 5+3
# 顯示8
