def isprime(n):

    for i in range(1, n+1, 1):
        if n % i != 0:
            return print(i)


def main():
    n = int(input("정수를 입력하세요: "))
    print(isprime(n))


main()
