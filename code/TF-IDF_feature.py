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
import sys
import string
#使此程序可以进行输出操作
stdout = sys.stdout
reload(sys)
sys.stdout = stdout
print 'can print something'

sys.setdefaultencoding( "utf-8" )
sys.path.append("F:")

#from numpy import *
fr = open(r'F:\study\master of TJU\DF\Sogou\DF-competition-sogou\data\sex\sex1_for_test.txt')
fr_list = fr.read()
dataList = fr_list.split('\n')
data = []#一行数据，用空格隔开
for oneline in dataList:
    #print oneline 可以打印出来每行的内容
    print 'line break'
    data.append(" ".join(jieba.cut(oneline))) 

#将得到的词语转换为词频矩阵
freWord = CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频，但我们只有一行
FT = freWord.fit_transform(data)
print freWord.get_feature_names()[55]#三国演义
#print FT.toarray()
print 'have',FT.toarray().sum(axis=0)[55]#输出每个特征词的总个数，正确，4个三国演义
#统计每个词语的tf-idf权值
transformer = TfidfTransformer()
#计算出tf-idf(第一个fit_transform),并将其转换为tf-idf矩阵(第二个fit_transformer)
tfidf = transformer.fit_transform(FT)
#获取词袋模型中的所有词语
word = freWord.get_feature_names()#获取词袋模型中的所有词语
#得到权重
weight = tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
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
fw = open(r'F:\study\master of TJU\DF\Sogou\DF-competition-sogou\data\sex\result_sex1_for_test.txt','w')
for i in sorted_tfidf:
	fw.write(i[0] + '\t' + str(i[1]) +'\n')