from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from tokenize import String
from konlpy.tag import Okt
import random

path = "./test3.pdf"

rsrcmgr = PDFResourceManager()
retstr = StringIO()
codec = 'utf-8'
laparams = LAParams()

f = open('./out.html', 'wb')
device = HTMLConverter(rsrcmgr, f, codec=codec, laparams=laparams)

fp = open(path, 'rb')
interpreter = PDFPageInterpreter(rsrcmgr, device)
password = ""
maxpages = 0
caching = True
pagenos = set()

for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
    interpreter.process_page(page)

fp.close()
device.close()
str = retstr.getvalue()
retstr.close()
f.close()
