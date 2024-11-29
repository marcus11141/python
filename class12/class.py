# list行帶轉換
print(range(10))  # 產生一個range但是看不到裡面的數字
print(list(range(10)))  # 將range轉換成list
print(list("Hello"))  # 將字串轉換成list

# split (Cut a string into pieces)
s = "Hello World"
L = s.split(" ")  # 將字串以空白分割
print(L)
calendar = "2020/12/25"
L = calendar.split("/")  # 將字串以/分割
print(L)

# join (Concatenate a list into a string)
L = ["Hello", "World"]
s = " ".join(L)  # 將list以空白合併
print(s)

# append (Add something new at the end)
L = ["Hello", "World"]
L.append("Python")  # 加入python
print(L)

# remove (Take somethig out)
L = ["Hello", "World", "Python"]
L.remove("World")  # 移除World
print(L)

# pop (Take out and remember)
L = ["Hello", "World", "Python"]
s = L.pop()  # 移除索引1的元素
print(s)

# count(Jow manny are there?)
L = ["Hello", "World", "Python", "Hello"]
print(L.count("Hello"))  # Hello出現幾次
