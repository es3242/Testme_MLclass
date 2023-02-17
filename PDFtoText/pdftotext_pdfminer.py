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

path = "./test3.pdf"

fp = open(path, 'rb') # 읽어올거
rsrcmgr = PDFResourceManager()
retstr = StringIO()
print(type(retstr))
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
        print(data)
        
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
    pdf_bypage[i] = pdf_bypage[i].replace("\n", "")

fp.close()

# 내용 보면서 디버깅할때 쓰면됨
# print(pdf_bypage[5])
# print(len(pdf_bypage))



