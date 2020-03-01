
print("종료하려면 음수를 입력하시오.")

리스트 = []
count = 0
while True:
    성적 = int(input("성적을 입력하시오 : "))
    if 성적 < 0:
        break
    리스트 .append(성적)  # 리스트에 입력한 성적이 하나씩 추가됨.
    count = count + 1

# len으로 카운트를 대신하여 사용할 수 있음.

sum = 0
for i in 리스트:
    sum = sum + i

avr = sum / count

print("성적의 평균은 %2s 입니다." % avr)

# for i in range(리스트):  # 리스트 안의 요소들을 꺼내서 더하고 싶음.
#sum = sum + i
#평균 = sum / count
# print(평균)
