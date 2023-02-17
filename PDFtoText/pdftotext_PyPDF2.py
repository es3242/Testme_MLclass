import PyPDF2

file = open("./test3.pdf", "rb")
fileReader = PyPDF2.PdfFileReader(file)

fileReader.pageMode

# 문서의 정보를 읽어들인다
fileReader.documentInfo

# 전체 페이지수를 출력한다.
print(fileReader.numPages)

# 페이지별로 정보를 가져온다
for i in range(0, fileReader.numPages):
    pageObj = fileReader.getPage(i)
    # 페이지 정보의 텍스트를 가져온다
    text = pageObj.extract_text()
    print('%d번째 페이지 원본 시작' % i)
    print('--------------------------------------')
    print(text)
    print('%d번째 페이지 원본 끝' % i)
