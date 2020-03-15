# GUI 모듈
#   turtle
#   tkinter ( --리눅스에서 tk/tcl 언어를 파이썬으로 포팅 한 것이다.)

from tkinter import *
from tkinter.filedialog import asksavesafilename
from tkinter.filedialog import askopenfilename

readFile = askopenfilename()  # 절대경로로 표시되는 파일명.


def main():


    # 파일의 존재 여부 체크
if readFile != None:
    # 파일열기
    infile = open(readFile, "r", encoding="UTF-8")  # 파일열기

    for line in infile.readlines():
        line = line. strip()  # 양쪽의 공백을 제거
        print(line)  # 표준(모니터)출력

        # 파일 닫기
    infile. close()
else:
    print("파일 없음")

if __name__ == "__main__":
    main()
