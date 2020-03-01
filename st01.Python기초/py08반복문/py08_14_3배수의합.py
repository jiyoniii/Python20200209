#i = 1
# while i < 100:
#    str = i % 3
#    if str == 0:
#        sum = str + str
#        print(str)
#    else:
#        str = str + 1


i = 1
sum = 0
while i <= 100:
    if i % 3 == 0:
        sum = sum + i
    else:
        i = i+1

print(sum)
