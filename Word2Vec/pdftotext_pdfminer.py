from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter, XMLConverter, TextConverter
from pdfminer.pdfdocument import PDFDocument
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import os
from io import StringIO
from tokenize import String
from konlpy.tag import Okt
import random
import re

path = "./test3.pdf"

def mining(path):
    fp = open(path, 'rb') # 읽어올거
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    # print(type(retstr))
    codec = 'utf-8'
    laparams = LAParams()

    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    pdf_bypage = []
    page_no = 0

    for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
        if pageNumber == page_no:
            interpreter.process_page(page)
            data = retstr.getvalue()
            # print(data)
            
            pdf_bypage.append(data)

            # 페이지 단위로 파일 나눠서 기록할때 쓰면됨
            # f = open('./out%d.txt' % page_no, 'wb') # 출력할거
            # f.write(data.encode("utf-8"))
            # f.close()

            data = ''
            retstr.truncate(0)
            retstr.seek(0)

            page_no += 1
    
    for i in range(0, len(pdf_bypage)):
        pdf_bypage[i] = ''.join([s for s in pdf_bypage[i].strip().splitlines(True) if s.strip()])
    pdf_bypage = ''.join(map(str, pdf_bypage))

    # print(pdf_bypage)

    fp.close()

    return pdf_bypage

test = mining(path)

print(type(test))

f = open('./test.txt', 'wb') # 출력할거
f.write(test.encode("utf-8"))
f.close()


'''
f = open('./pdf2txt.txt', 'wb') # 출력할거
for i in range(0, len(test)):
    for r in range(0, len(test[i])):
        print(test[i][r])
        # f.write(test[i][r].encode("utf-8"))
    # test[i] = test[i].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "")
    # re.compile('[가-힣]+').findall(test[i])
    # test[i] = re.sub(r"[^ㄱ-ㅣ가-힣\s ]", "", test[i]) # 한글 외 제거
    # test[i] = re.sub(' +', '', test[i]) # 연속 공백 제거
    # test[i] = re.sub("\n+", ' ', test[i]) # 연속 줄바꿈 제거
f.close()
'''

# print(test)

# 내용 보면서 디버깅할때 쓰면됨
# print(pdf_bypage[5])
# print(len(pdf_bypage))



