# ▪ 순서도1
# 정수를 입력 받고 '시작값' 변수에 저장하시오
# 정수를 입력 받고 '종료값' 변수에 저장하시오
#
# 시작값이 종료값보다 크다면
#     i 는 종료값부터 시작값까지 i를 1씩 증가시키면서 합계를 구해하시오
# 아니면
#     i 는 시작값부터 종료값까지 i를 1씩 증가시키면서 합계를 구해하시오
#
# 합계를 출력하시오

#
# ▪ 순서도2
# 정수를 입력 받고 '시작값' 변수에 저장하시오
# 정수를 입력 받고 '종료값' 변수에 저장하시오
#
# 시작값이 종료값보다 크다면
#         종료값을  temp에 넣는다.
#         시작값을 종료값 에 넣는다.
#         temp을 시작값에 넣는다.
# 아니면
# i 는 시작값부터 종료값까지 i를 1씩 증가시키면서 합계를 구해하시오.
#
# 합계를 출력하시오.

# ▪ 실행결과예시
# 시작값을 입력하세요.  1
# 종료값을 입력하세요.  4
# 1부터 4까지의 합계는 10입니다
#
# ▪ 실행결과예시
# 시작값을 입력하세요.  4
# 종료값을 입력하세요.  1
# 1부터 4까지의 합계는 10입니다

x = int(input("시작값을 입력하시오 : "))
y = int(input("종료값을 입력하시오: "))

if x > y:
    temp = x
    x = y
    y = temp
else:
    pass

sum = 0
for i in range(x, y+1, 1):
    sum = sum + i

str = "%s 부터%s 까지의 합계는 %s 입니다." % (x, y, sum)
print(str)
