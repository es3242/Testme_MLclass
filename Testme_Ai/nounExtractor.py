import os
from tokenize import String
from konlpy.tag import Okt
from pdftotext_pdfminer import mining

Okt = Okt()

def nounExtractor(path):
    try:    
        writeLine = mining(path).copy()
        nounsLine = []
        nouns = []
        pages = len(writeLine)
        
        for i in range (pages):
            line = writeLine[i]# 한줄 씩 읽어 옴
            if not line: break # 파일 끝 까지 반복
            nouns = Okt.nouns(line) #한 줄에 있는 명사들 모두 nouns에 저장 (리스트)

            if len(nouns) == 0 : 
                nounsLine.append(' ')
                continue #명사 없을 경우 ' ' 저장 후 pass
            line= ' '.join(map(str, nouns))
            nounsLine.append(line)

        print('nounExtractor 정상작동 ',pages,'페이지 확인')
        return(nounsLine)
    except:
        print('error')

print(nounExtractor("./test3.pdf"))

