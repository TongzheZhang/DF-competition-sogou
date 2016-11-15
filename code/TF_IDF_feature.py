# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 20:39:11 2016

@author: Richard
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:09:50 2016

@author: Richard
IF_IDF特征的理解：http://blog.csdn.net/liuxuejiang158blog/article/details/31360765?utm_source=tuicool&utm_medium=referral
已完成除去停顿词的特征提取工作
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
#stdout = sys.stdout
#reload(sys)
#sys.stdout = stdout
#print 'can print something'

#设置系统编码方式为utf-8
#sys.setdefaultencoding( "utf-8" )
#sys.path.append("F:")

#读入停顿符号和待提取文本



fr = open(r'F:\study\master of TJU\DF\Sogou\DF-competition-sogou\data\age_test.txt')
fr_list = fr.read()
dataList = fr_list.split('\n')
data = []#还是原行数数据，词用空格隔开



stopwords = {}.fromkeys([ line.rstrip().decode('utf8') for line in open('stopwords.txt') ])
blanklist = [' ','\t','']

for oneline in dataList:
    #print oneline 可以打印出来每行的内容
    #print oneline
    print 'line break'
    temp = []
    for i in jieba.cut(oneline):
        if i not in stopwords:
            if i not in blanklist:
                temp.append(i)
    data.append(" ".join(temp)) #'sep'.join(seq)，分隔符为空格，原来的一行还是一行
    
print data[0]
print data[1]
print data[2]


#将得到的词语转换为词频矩阵
#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频，但我们只有一行
freWord = CountVectorizer(ngram_range=(1, 1))
FT = freWord.fit_transform(data)
print type(FT)
print FT.toarray()
'''
print freWord.get_feature_names()[55]#三国演义
print FT.toarray()
print 'have',FT.toarray().sum(axis=0)[55]#输出每个特征词的总个数，正确，4个三国演义
'''
#统计每个词语的tf-idf权值
transformer = TfidfTransformer()
#计算出tf-idf(第一个fit_transform),并将其转换为tf-idf矩阵(第二个fit_transformer)
tfidf = transformer.fit_transform(FT)#其实就是对数组进行计算
#获取词袋模型中的所有词语
word = freWord.get_feature_names()#获取词袋模型中的所有词语
print '特征维度：',len(word)
for i in word:
    print i
    
testsen = '韩 柔和 陶喆 首页'
testsenlist = []
testsenlist.append(testsen.decode('utf8'))


print 'testdata的词频向量，',freWord.transform(testsenlist).toarray()

    
#得到权重
weight = tfidf.toarray()#将tf-idf矩阵取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
print '训练集第一句话的特征'
print tfidf[0]
idxofNZ = sorted(tfidf[0].nonzero()[1])
print idxofNZ
for i in idxofNZ:
    print tfidf[0,i]


'''
print '三国演义在不同文本中的TF-IDF值，他只在第一行出现过四次'
print weight[0][55]
print weight[1][55]
'''

result = transformer.transform(freWord.transform(testsenlist).toarray())
print result.nonzero()
print result.toarray()
'''
tfidfDict = {}

#得到全局TFIDF值
for i in range(len(weight)):#遍历所有文本文本
    for j in range(len(word)):#遍历某一类文本下的词语权重
        getWord = word[j]
        getValue = weight[i][j]
        if getValue != 0: #去掉值为0的项
            if tfidfDict.has_key(getWord):
                tfidfDict[getWord] += string.atof(getValue)
            else:
                tfidfDict.update({getWord:getValue})
#返回一个排序后的列表
sorted_tfidf = sorted(tfidfDict.iteritems(),#这是字典的迭代器
					  key = lambda d:d[1],reverse = True)#这个key表示按照第一列的大小排列，即权重
fw = open(r'F:\study\master of TJU\DF\Sogou\DF-competition-sogou\data\result_age_for_test.txt','w')#w是新建
for i in sorted_tfidf:
	fw.write(i[0] + '\t' + str(i[1]) +'\n')
 '''