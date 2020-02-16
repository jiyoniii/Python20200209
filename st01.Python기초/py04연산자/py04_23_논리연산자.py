x = 3
y = 4

r = ((x==3) and (y ==3))
print ("(x ==3) and (y==3) : ", r)  #false

r = ((x==3)and (y != 3))
print ("(x == 3) and (y !=3) : ", r) #true

r = ((x ==3) or (y ==3)) 
print ("(x ==3) or (y ==3) : ", r) #true

r = ((x == 3) or (y == 4))
print ("(x == 3) or (y == 4) : " , r) #true

r = ((x != 3) or (y == 4))
print ("( x !=3) or ( y==4 ) : ", r) #true

r = ((x !=3) or (y != 4))
print ("(x !=3) or (y != 4) : ", r) #false

#변수선언과 초기화
x = 3
y = 4

print ((x ==y) and (x != y) #false
print ((x >y)  or (x < y)) #true
print ((x >= y) or (x <=y)) #true
print ((x ==y) and (x !=y) or (x< y )) #true