# -*- coding: utf8 -*-
import jieba
import codecs
import math
import jieba.analyse 
import io
import numpy as np

## 停用词
def stopwordslist(filepath):  
    stopwords = [line.strip() for line in io.open(filepath, 'r',encoding='utf-8').readlines()]  
    return stopwords  
  
###获取TF-IDF  关键词
def get_keywords(text):
    seg = jieba.cut(text) 
    jieba.analyse.set_stop_words('/Users/ppj/DeepLearning_project/ppj_text_similarity/stopwords.txt')  
    keyWord = jieba.analyse.extract_tags( '|'.join(seg), topK=20, withWeight=True, allowPOS=())#在这里对jieba的tfidf.py进行了修改  
    
    return keyWord

##  分词  去停用词
def seg_sentence(sentence):  
    sentence_seged = jieba.cut(sentence.strip())  
    stopwords = stopwordslist('/Users/ppj/DeepLearning_project/ppj_text_similarity/stopwords.txt')  # 这里加载停用词的路径  
    outstr =[]  
    for word in sentence_seged:  
        if word not in stopwords:  
            if word != '\t':  
                outstr.append(word)  
    return outstr       


def keywords_set(text1,text2):
    keyword_1 = get_keywords(text1)
    keyword_2 = get_keywords(text2)
    keywordslist=set([])
    for key1 in keyword_1:
        keywordslist.add(key1[0])
    for key2 in keyword_2:
        keywordslist.add(key2[0])
    
    return list(keywordslist)

### 词频向量
def vector_list(text1,text2):
    keywordslist=keywords_set(text1,text2)
    doc_a_list=seg_sentence(text1)
    doc_b_list=seg_sentence(text2)
    #计算向量
    vector_a = []
    vector_b = []
    length = len(keywordslist)
    length_a = len(doc_a_list)
    length_b = len(doc_b_list)
    for x in range(0,length):
        vector_a.append(doc_a_list.count(keywordslist[x]))
 
    for m in range(0,length):
        vector_b.append(doc_b_list.count(keywordslist[m]))

    return np.array(vector_a),np.array(vector_b)

#计算余弦值
def compute_cossim(text1,text2):
    vector_a,vector_b=vector_list(text1,text2)
    fz=np.sum(vector_a*vector_b)
    fm_a=np.sqrt(np.sum(vector_a**2))
    fm_b=np.sqrt(np.sum(vector_b**2))
    prob=fz/float((fm_a*fm_b))
    print '文档相似度: '
    return prob

if __name__ == '__main__':

    
    file1 = '/Users/ppj/DeepLearning_project/ppj_text_similarity/input_6.txt'
    text1=io.open(file1,'r',encoding='utf-8').readlines()[0]

    file2 = '/Users/ppj/DeepLearning_project/ppj_text_similarity/input_5.txt'
    text2=io.open(file2,'r',encoding='utf-8').readlines()[0]

    
    print compute_cossim(text1,text2)




