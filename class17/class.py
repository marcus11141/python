a = ["a", "b", "c"]
b = a  # 把a的"記憶體位置"指定給b，所以a和b指向同一個"記憶體位置"
b[0] = "d"  # 把b的第一個元素，a也會跟著改變
print(a)  # 顯示:["d", "b", "c"]

a = 10
b = a  # 把a的"值"指定給b，所以a和b的"值"相同
b = 20  # 修改b的值，a不會改變
print(a)  # 顯示:10
