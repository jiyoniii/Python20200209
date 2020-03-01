def isprime(n):

    for i in range(2, n, 1):
        if n % i == 0:
            return False
        else:
            return True


def myinput(mesg):
    try:
        n = input(mesg)
        n = int(n)
    except ValueError as ex:
        print(ex)
    return n



def main():
    n = myinput("정수를 입력하세요 : ")
    print(isprime(n))


main()
