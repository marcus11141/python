# index 找出元素在清單中的位置
L = [1, 3, 2, 4, 5]
print(L.index(3))  # 1

# sort 排序, 預設是是由小到大
L = [1, 3, 2, 4, 5]
L.sort()
print(L)

# sort reverse, 由大到小
L = [1, 3, 2, 4, 5]
L.sort(reverse=True)
print(L)

# reverse 反轉清單當中的元素, 不是排序
L = [1, 3, 2, 4, 5]
L.reverse()
print(L)

# 字典
# 建立字典
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d)


# 取得字典的鍵
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d["蘋果"])
# print(d{"梨子"}) # KeyWrror: '梨子'

# len 取得字典的長度
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(len(d))
# 檢查key是否存在
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print("蘋果" in d)  # True
print("梨子" in d)  # False

# 字典走訪
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
for k in d:
    print(k)  # 這樣會只印出key
    print(d[k])  # 這樣會印出value

for k in d.keys():
    print(k)  # 這樣會印出key
    print(d[k])  # 這樣會印出value

for v in d.values():
    print(v)  # 這樣會印出value

for k, v in d.items():
    print(k, v)  # 這樣會印出key, value
