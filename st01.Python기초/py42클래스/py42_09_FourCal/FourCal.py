
# 작업 순서
# 1. 모듈 또는 클래스 import
# 2. 클래스명은 파스칼 표기법으로 정한다. 첫글자는 대문자로.
#     생성자 선언 : 인스턴스가 생성될 때 실행
#     소멸자 선언 : 소멸자는 인스턴스가 소멸할 때 실행
#     __str__() 메서드 오버라이딩
#     접근자( getter ) 메서드 선언. 비공개 인스턴스 변수 읽기
#     설정자( setter ) 메서드 선언. 비공개 인스턴스 변수 수정
#     사용자 메서스 선언
# 3. main() 메서드 만들기
#     인스턴스 생성
# 4. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()


# 코딩 하기

import math


class FourCal:
    def __init__(self, first, second):  # 생성자
        self.__first = first
        self.__secont = second

    def add(self):  # 여기부터는 사용자메서드
        result = self.__first + self.__second
        return result

    def minus(self):
        result = self.__first - self.__second
        return result

    def mul(self):
        result = self.__first * self.__second
        return result

    def div(self):
        result = self.__first / self.__second
        return result

# 비공개 변수 선언 시, 각 변수 당 getter,setter 1세트씩 만들어줘야함.
# getter는 무조건 return이다.
# getter 메서드의 목적 : 비공개 변수값을 리턴한다.

    def getFirst(self):
        return self.__first  # 비공개 first를 리턴해라.

# setter 메서드의 목적 : 비공개 변수값을 바꾼다.
    def setFirst(self, num):
        self.__first = num

    def getSecond(self):
        return self.__second

    def setSecond(self, num):
        self.__second = num


def main():
    # 인스턴스 만들기
    c1 = FourCal(4)

    # 비공개 변수 self.__first 값을 출력
    val = c1.getFirst()
    print(val)  # 4가 프린트됨/
    # 비공개 변수 self.__first 값을 8로 바꾸시오.
    c1.first = 8  # 변경 안됨.


main()
