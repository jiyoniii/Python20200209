x = 1
y = 4
z = 5


#중첩 if 방식
if x >y :
    #x, z를 비교한다.
    if x>z:  #if대신 and로 바꿀 수 있음.
        print(x)
    else:
        print(z)

else :
    #y와 z를 비교한다.
    if y>z :
        print(y)
    else : 
        print(z)

#연속 if 방식

if x>y and x>z :
    print(x)
elif y>z :
    print(y)
else:
    print(z)