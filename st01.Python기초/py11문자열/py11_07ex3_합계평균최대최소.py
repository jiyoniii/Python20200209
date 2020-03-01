def main():
    lst = temp3.split(" ")
    print(type(lst), lst)

    # lst는 0번부터 시작한다.
    print(lst[0])  # 74
    print(lst[1])  # 874

    # 문자열을 정수 리스트로 만든다.
    lst[0] = int(lst[0])
    print(lst[0], type(lst[0]))

    for i in range(0, len(lst), 1):
        lst[i] = int(lst[i])
    print(type(lst), lst)

    # 오름차순으로 정리
    lst = sorted(lst)
    print(lst)

    # 합계,평균,최대값, 최소값 구하기
    print()

if __name__ == "__name__":
    main()
