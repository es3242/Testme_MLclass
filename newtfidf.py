from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
from newnounExtractor import nounExtractlist
from newblankMaker import makeBlanks 

def tf_idf(input):
    documents = nounExtractlist(input)
    vectorizer = CountVectorizer()
    dtm = vectorizer.fit_transform(documents)

    tf = pd.DataFrame(dtm.toarray(), columns = vectorizer.get_feature_names_out())
    df = tf.astype(bool).sum(axis = 0)
    D = len(tf)

    # Inverse Document Frequency - IDF 계산
    idf = np.log((D+1) / (df+1)) + 1
    # TF-IDF
    tfidf = (tf * idf) / np.linalg.norm((tf * idf), axis = 1, keepdims = True)

    return tfidf

def makeTest(input,output):

    #답(중요 키워드) 
    solutions = list(tf_idf(input).idxmax(axis=1).fillna(0))

    #빈칸 생성
    result = makeBlanks(input,solutions)

    f = open(output,"w",encoding = 'utf-8')

    for i in range(len(result)):
        f.write("slide %d\n" %(i+1))
        f.write(result[i]+"\n")
        
    f.write("\n답지\n")

    for i in range(len(solutions)):
        if(solutions[i] == 0):
            continue
        f.write("%d번 답: %s\n" %((i+1) ,solutions[i]))
        
    f.close()

#makeTest("./samplePdf/test3.pdf","./sampleOutput/problem1.txt")
makeTest("../samplePdf/sample1.pdf","../sampleOutput/sample1.txt")

