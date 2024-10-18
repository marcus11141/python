# import turtle as t

# t.speed(0)
# t.color("red")
# t.shape("square")
# t.penup()

# for i in range(500):
#     t.stamp()

#     t.right(50)
#     t.forward(10 + i)
# t.done()
num = int(input("請輸入數字:"))
sum = 0
for i in range(num + 1):
    sum = sum + i

print(f"到{num}的總和是{sum}")
