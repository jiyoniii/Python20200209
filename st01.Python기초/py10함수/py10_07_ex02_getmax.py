def getmax(x, y):
    if(x > y):
        return x
    else:
        return y


def myinput(mesg):
    try:
        n1 = input(mesg)
        n1 = int(n1)
    except ValueError as ex:
        print(ex)

    return n1


def main():
    n1 = myinput("첫 번째 정수 입력 : ")
    n2 = myinput("두 번째 정수 입력 : ")

    val = getmax(n1, n2)
    print(val)


main()
