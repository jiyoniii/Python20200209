
x = 2
for x in range(1, 10, 1):
    print("2 * ", x, "=", 2*x)

for x in range(1, 10, 1):
    print("2 * %s = %s" % (x, 2*x))  # %d를 사용하여도 됨.
