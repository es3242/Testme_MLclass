# -*- coding: utf-8 -*-

import os
from tokenize import String
from konlpy.tag import Okt
import random
from pdftotext_pdfminer import mining

Okt = Okt()

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
