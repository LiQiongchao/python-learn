
"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

"""
x = int(input("请输入x: "))

if x > 1:
    y = 3 * x - 5
elif x < -1:
    y = 5 * x + 3
else:
    y = x + 2
print("f(%.0f) = %.2f" %(x, y))



