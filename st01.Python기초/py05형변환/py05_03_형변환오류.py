
# 숫자가 아닌 것을 정수로 변환하려고 할 때
#try가 나오게 하려면 tr 입력 후 컨트롤+스페이스 입력 후 except 선택
try :
    i = int("안녕하세요")
    print(i) #문장이 실행되지 않음.
except ValueError :
    pass #넘어간다.


# 숫자가 아닌 것을 실수로 변환 할 때
try :
    f = float("안녕하세요")
except ValueError : 
    pass

# 소수점이 있는 숫자 형식의 문자열을 int() 함수로 변환 할 때
