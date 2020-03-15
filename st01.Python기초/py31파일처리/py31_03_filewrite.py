# 소스 실행 시 오류가 있습니다. 아래의 수정사항을 적용하시오.
#   1.파일 열 때 utf==8 인코딩을 설정하시오.
#   2.파일은 상대경로로 설정하시오.


# 아래내용 작업 후 터미널(py31파일처리 폴더에서 우클릭 후 open terminal)
# 에서 python .\py31_03_filewrite.py 입력.
# 파일이 생성되고 글이 입력되어있음.

outfile = open("phones.txt", "w")

if os.path.isfile("phones.txt"):
    outfile.write("홍길동 010-1234-5678\n")
    outfile.write("김철수 010-1234-5679\n")
    outfile.write("김영희 010-1234-5680\n")
    #print("동일한 이름의 파일이 이미 존재합니다.")
else:
    #outfile.write("홍길동 010-1234-5678")
    #outfile.write("김철수 010-1234-5679")
    #outfile.write("김영희 010-1234-5680")
    print("완료")

outfile.close()
