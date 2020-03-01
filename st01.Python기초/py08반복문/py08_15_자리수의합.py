
정수 = input("정수입력")

length = len(정수)

sum = 0
for i in range(0, length, 1):
    x = int(정수[i])
    sum = sum+x
print(sum)
