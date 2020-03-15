
#  proverbs.txt 파일에서 줄 단위로 읽어서 output.txt 에 쓰시오

f = open("./st01.Python기초/py31파일처리/file/proverbs.txt", "r",)


line = f.readline()
while line != "":
    # 모니터에 출력
    print(f, end="")  # 모니터에 출력

    # 다시 파일에서 읽기
    # line = f.readline()  # 한 줄 읽기

f.close()
# f2.close()
#output = open("output.txt", "w")


#outfile = open("phones.txt", "a")

#outfile.write("최무선 010-1111-2222\n")
#outfile.write("정중부 010-2222-3333\n")

# outfile.close()
