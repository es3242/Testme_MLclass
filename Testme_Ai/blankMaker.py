# -*- coding: utf-8 -*-

import os
from tokenize import String
from konlpy.tag import Okt
import random
from pdftotext_pdfminer import mining

Okt = Okt()

# for x in range(15):
#     text = f.readline() # 한줄 씩 읽어 옴
#     print(text) # 읽어온 문장 출력
#     #print(len(Okt.nouns(text))) #문장에 있는 명사의 길이 출력
#     nouns = Okt.nouns(text) #문장에 있는 명사 nouns에 저장 (리스트)
#     #print(nouns) #문장에 있는 명사 출력


#     for i in range (len(nouns)): # 명사 길이 만큼
#         text = text.replace(nouns[i], '( )') # word와 일치 하는 단어를 ()로 교체 해서 다시 저장
#     print(text)
    
def makeBlanks(path,dict): #매개변수 1.읽어드릴 파일, 2.생성할 파일명 2.생성할 빈칸 갯수 (1~3)
    try:    
        writeLine = mining(path).copy()

        for i in range(len(dict)):
            line = writeLine[i] # 한줄 씩 읽어 옴
            if not line: break # 파일 끝 까지 반복

            if dict[i] == 0 : 
                continue #명사 없을 경우 pass

            line = line.replace(dict[i], '( )')
            writeLine[i] = line
        
        return writeLine

    except:
        print('error')
            
                

        #단어 2,3개 생성 시
        # if blank == 2:
        #     while True:
        #         line = f1.readline() # 한줄 씩 읽어 옴
        #         if not line: break # 파일 끝 까지 반복
        #         nouns = Okt.nouns(line) #한 줄에 있는 명사들 모두 nouns에 저장 (리스트)

        #         if len(nouns) == 0 : 
        #             continue #명사 없을 경우 pass

        #         if len(nouns) == 1 : # 명사 한 개일 경우
        #             line = line.replace(nouns[0], '( )')
        #             f2.write(line)
        #             continue

        #         ranNum = random.sample(range(len(nouns)),2) # 0~명사 길이 범위 에서 랜덤 숫자 2개 추출
        #         for i in range (2): # 명사 2개 이상일 경우, 2번 반복. '()' 2개 생성이므로
        #             line = line.replace(nouns[ranNum[i]], '( )') # word와 일치 하는 단어를 ()로 교체 해서 다시 저장           
                
        #         f2.write(line)

        # if blank == 3:
        #     while True:
        #         line = f1.readline() # 한줄 씩 읽어 옴
        #         if not line: break # 파일 끝 까지 반복
        #         nouns = Okt.nouns(line) #한 줄에 있는 명사들 모두 nouns에 저장 (리스트)

        #         if len(nouns) == 0 : continue #명사 없을 경우 pass

        #         if len(nouns) == 1 : # 명사 한 개일 경우
        #             line = line.replace(nouns[0], '( )')
        #             f2.write(line)
        #             continue

        #         ranNum = random.sample(range(len(nouns)),2) # 0~명사 길이 범위 에서 랜덤 숫자 2개 추출      
        #         if len(nouns) == 2 : # 명사 2개 일 경우
        #             for i in range (2):  
        #                 line = line.replace(nouns[ranNum[i]], '( )') # word와 일치 하는 단어를 ()로 교체 해서 다시 저장
        #             f2.write(line)
        #             continue

        #         ranNum = random.sample(range(len(nouns)),3) # 0~명사 길이 범위 에서 랜덤 숫자 3개 추출
        #         for i in range (3): # 명사 3개 이상일 경우, 3번 반복. '()' 3개 생성이므로
        #             line = line.replace(nouns[ranNum[i]], '( )') # word와 일치 하는 단어를 ()로 교체 해서 다시 저장          




#makeBlanks('indext2.txt','new.txt',2) #빈칸 1개 생성할 경우



