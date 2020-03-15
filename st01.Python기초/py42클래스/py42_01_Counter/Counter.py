
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


class Counter:
    # 생성자 메서드 선언. 생성자 중복 불가. 1개만 존개 가능.
    def __init__(self):  # 메서드(동작,동사)
        self.__count = 0  # 변수(=함수)(상태,명사)

    def reset(self):
        self.__count = 0

    def increment(self):
        self.__count += 1

    def getCounter(self):
        return self.__count

    # def setCount(self):
    #    self.increment()
        # 클래스 안에서만 self를 씀. class안에 있는 메소드가 다른 메소드를 호출할 때 self가 앞에 붙음.


def main():
    print()


if __name__ == "__main__":
    main()
