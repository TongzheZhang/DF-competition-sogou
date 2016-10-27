# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:09:50 2016

@author: Richard
"""

# -*- coding: cp936 -*-
import jieba
import jieba.posseg as pseg
import os
import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from numpy import *
import string
#reload(sys)后无法使用print，使用以下办法可以使用print
stdout = sys.stdout
reload(sys)
sys.stdout = stdout

sys.setdefaultencoding( "utf-8" )
sys.path.append("F:\study\master of TJU\DF\Sogou\DF-competition-sogou\data")
#from numpy import *
fr = open(r'F:\study\master of TJU\DF\Sogou\DF-competition-sogou\data\sex\sex1_for_test.txt')
fr_list = fr.read()
dataList = fr_list.split('\n')


data = []





for oneline in dataList: 
    print 'i am running... in 1'
    data.append(" ".join(jieba.cut(oneline)))    


#将得到的词语转换为词频矩阵
freWord = CountVectorizer()
#统计每个词语的tf-idf权值

print 'i am running... in 2'
transformer = TfidfTransformer()
#计算出tf-idf(第一个fit_transform),并将其转换为tf-idf矩阵(第二个fit_transformer)
tfidf = transformer.fit_transform(freWord.fit_transform(data))
#获取词袋模型中的所有词语
word = freWord.get_feature_names()
print 'i am running... in 3'
#得到权重
weight = tfidf.toarray()
print 'i am running... in 4'
tfidfDict = {}
for i in range(len(weight)):
	for j in range(len(word)):
		getWord = word[j]
		getValue = weight[i][j]
		if getValue != 0:
			if tfidfDict.has_key(getWord):
				tfidfDict[getWord] += string.atof(getValue)
			else:
				tfidfDict.update({getWord:getValue})
sorted_tfidf = sorted(tfidfDict.iteritems(),
					  key = lambda d:d[1],reverse = True)
fw = open(r'F:\study\master of TJU\DF\Sogou\DF-competition-sogou\data\sex\result_of_sex1_for_test.txt','w')
for i in sorted_tfidf:
	fw.write(i[0] + '\t' + str(i[1]) +'\n')
