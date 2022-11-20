import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from nounExtractor import nounExtractor
from blankMaker import makeBlanks 

path = "./test3.pdf"
documents = nounExtractor(path)
vectorizer = CountVectorizer()


# Document Term Matrix, 명사추출 결과 값인 Document에 CountVectorizer적용.
dtm = vectorizer.fit_transform(documents)
# Term Freqeuncy, 전체 카운팅 된 행렬을 단어들의 이름을 열의 이름으로 하는 행렬로 만들어서 tf로 저장함.
tf = pd.DataFrame(dtm.toarray(), columns = vectorizer.get_feature_names_out())
# Document Frequency , 전체 슬라이드에서의 단어의 출현 횟수를 구해 df에 저장함
df = tf.astype(bool).sum(axis = 0)
# 문서 개수
D = len(tf)

# Inverse Document Frequency - IDF 계산
idf = np.log((D+1) / (df+1)) + 1
# TF-IDF
tfidf = tf * idf                      
tfidf = tfidf / np.linalg.norm(tfidf, axis = 1, keepdims = True)

#답(중요 키워드) 임
lista = list(tfidf.idxmax(axis=1).fillna(0))
print(lista)

#빈칸 생성
result = makeBlanks(path,lista).copy()

# txt 파일로 추출하는 부분

f = open("output.txt","w")

for i in range(D):
    f.write("slide %d\n" %(i+1))
    f.write(result[i]+"\n")
    
f.write("\n답지\n")
for i in range(D):
    if(lista[i] == 0):
        continue
    f.write("%d번 답: %s\n" %((i+1) ,lista[i]))
    
f.close()