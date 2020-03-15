# 입력 파일 이름과 출력 파일 이름을 받는다.

# 입력과 출력을 위한 파일을 연다.

# 합계와 횟수를 위한 변수를 정의한다.

# 입력 파일에서 한 줄을 읽어서 합계를 계산한다.

# 총매출과 일평균 매출을 출력 파일에 기록한다.

# file open
salesFile = open(
    "C:\\python.20200209\\Python기초.20200209.실습용\\st01.Python기초\\py31파일처리\\file\\sales.txt", "r")
summary = open(
    "C:\\python.20200209\\Python기초.20200209.실습용\\st01.Python기초\\py31파일처리\\file\\summary.txt", "w")

# file process
sum = 0
count = 0
avg = 0

# read & print in for
# read 에서 덧셈 평균 구한 후 sumary로 넘기기.
# sales에 있는 파일 내용 통째로 넘기기.
for line in salesFile.readlines():
    line = int(line)
    sum = sum + line
    count = count + 1
    avg = sum / count
print("라인의 개수: ", count)
print("합계 : ", sum)
print("평균 : ", avg)

sum = str(sum)
avg = str(avg)
summary.write("합계 : " + sum)
summary.write("\n")
summary.write("평균 : " + avg)
# summary.write(encoding="UTF-8")

salesFile.close()
summary.close()
