from konlpy.tag import Okt
from pdfminerTest import extractlst

Okt = Okt()

input = "test3.pdf"

def nounExtractlist(input):
    arr = extractlst(input)
    nounslist = []
    for lines in arr:
        nouns = []
        nouns = Okt.nouns(lines)
        if len(nouns) == 0 : 
            nounslist.append(' ')
            continue
        nounslist.append(' '.join(map(str, nouns)))
    print(nounslist)
    return nounslist

def verbExtractlist(input):
    arr = extractlst(input)
    verbslist = []
    temp = []
    for lines in arr:
        tagging = Okt.pos(lines)
        if len(tagging) == 0 : 
            temp.append(' ')
            continue
        for i,j in tagging:
            if j == 'Verb':
                temp.append(i)
        verbslist.append(' '.join(map(str, temp)))
    print(verbslist)
    return verbslist

def adjExtractlist(input):
    arr = extractlst(input)
    adjslist = []
    temp = []
    for lines in arr:
        tagging = Okt.pos(lines)
        if len(tagging) == 0 : 
            temp.append(' ')
            continue
        for i,j in tagging:
            if j == 'Adjective':
                temp.append(i)
        adjslist.append(' '.join(map(str, temp)))
    print(adjslist)
    return adjslist

#print(verbExtractlist(input))