import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from pdftotext_pdfminer import mining
from nounExtractor import nounExtractor

path = "./test3.pdf"

documents = []
for i in range (len(nounExtractor(path))):
    line = nounExtractor(path)[i]
    documents.append(line)
print(documents)

vectorizer = CountVectorizer()

# Document Term Matrix
dtm = vectorizer.fit_transform(documents)

# Term Freqeuncy
tf = pd.DataFrame(dtm.toarray(), columns = vectorizer.get_feature_names_out())


df = tf.astype(bool).sum(axis = 0)


# 문서 개수
D = len(tf)

# Inverse Document Frequency
idf = np.log((D+1) / (df+1)) + 1

# TF-IDF
tfidf = tf * idf                      
tfidf = tfidf / np.linalg.norm(tfidf, axis = 1, keepdims = True)
tfidf.to_csv("houseprice.csv", index = False)