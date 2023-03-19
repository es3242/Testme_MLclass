from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

#txt 추출 함수
def extractTxt(input,output):
    f = open(output,"w",encoding = 'utf-8')
    for page_layout in extract_pages(input):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                f.write(element.get_text())
    f.close()


#페이지 당 리스트로 저장, 그 리스트를 반환하는 함수

def extractlst(input):
    lst = []   
    for page_layout in extract_pages(input):
        temp = []
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                temp.append(element.get_text())
        if len(temp) == 0:
            continue
        lst.append(''.join(temp))
    return lst

#extractTxt("test3.pdf","test.txt")
