
# 0번째부터 12번째 자리까지 있음.
# prov 길이는 13이다.
prov = "A barking Dog"


#################################
# 문자열 함수 / 문자열 메서드
#################################

# 문자열 길이: len().  prov의 길이를 출력하시오
print(len(prov))


# 첫번째 b 문자를 찾고 위치를 출력하시오.
# find와 index 모두 사용할 수 있지만, find로 하는것이 좋다. find로 할 때 못찾게되면 -1를 표시하지만, index는 에러로 표시한다.

print(prov.find("b"))


# 문자열에 "Dog"가 있으면 "Dog있음"을 없으면 "Dog없음" 을 출력하시오
# "Dog 있음"
if prov.index("Dog"):
    print("있음")
else:
    print("없음")

# 선생님이 푼 방식

pos = prov.find("Dog")
if pos == -1:
    print("Dog 없음")
else:
    print("Dog 있음")

# 문자열 치환: replace()
# prov 문자열에 Dog가 들어 있으면 Cat으로 바꾸어 출력하고
# 아니면 prov 출력하시오.
if prov.index("Dog"):
    print(prov.replace("Dog", "Cat"))
else:
    print(prov)

    # 문자열 prov 를 공백을 기준으로 자르고 그 결과를 출력하시오


print(prov.split(" "))

# 선생님이 한 방식

lst = prov.split(" ")
print(type(lst), lst)
