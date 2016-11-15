# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:07:08 2016

@author: Richard
自己实现的搜狗的程序
"""
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import jieba
from sklearn import svm 
import os
os.chdir(r'F:\study\master of TJU\DF\Sogou\DF-competition-sogou\code')
from svmutil import *
from time import sleep
import datetime

def read_text_src(text_src, delimiter = '\t'):
    if isinstance(text_src, str):
        with open(text_src, 'r') as f:
            text_src = [line.split(delimiter) for line in f]
    elif not isinstance(text_src, list):
        raise TypeError('text_src should be list or str')
    return text_src
    
if __name__ == "__main__":
    #print 'i am main'
    '''
    here!带标签的训练集
    print datetime.datetime.now()
    text_src = r'F:\study\master of TJU\DF\Sogou\DF-competition-sogou\data\age_final.txt'
    files = read_text_src(text_src)
    label = []
    dataList = []
    for line in files:
        #print line[0]
        t = int(line[0])
        label.append(t)
        dataList.append(line[1])
    #print len(label)
    #print len(files[0])
    print 'datalist维度',len(dataList)
    print datetime.datetime.now()
    data = []#还是原行数数据，词用空格隔开,perfect data
    here!考一个停用词库
    stopwords = {}.fromkeys([ line.rstrip().decode('utf8') for line in open('stopwords.txt') ])
    blanklist = [' ','\t','']
    corpus = {}.fromkeys([ line.rstrip().decode('utf8') for line in open('corpus.txt') ])  
    for oneline in dataList:
        #print oneline
        #print 'line break'
        temp = []
        #here!cut
        #两个cut须一致，下面还有一个cut
        for i in jieba.cut(oneline,cut_all=False):
            if i not in stopwords:
                if i not in blanklist:
                    if i in corpus:
                        temp.append(i)  
        data.append(" ".join(temp)) #'sep'.join(seq)，分隔符为空格，原来的一行还是一行
    print ' i finish reading trainingdata'
    print datetime.datetime.now()
    #print data[0]
    #print data[1]
    #print data[2]
    
    #将得到的词语转换为词频矩阵
    #该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频，但我们只有一行
    #here!可以选择几元！
    freWord = CountVectorizer(ngram_range=(1, 1))
    FT = freWord.fit_transform(data)
    print 'i finish counting words'
    #print FT
    #print FT.toarray()

    #统计每个词语的tf-idf权值
    transformer = TfidfTransformer()
    #计算出tf-idf(第一个fit_transform),并将其转换为tf-idf矩阵(第二个fit_transformer)
    tfidf = transformer.fit_transform(FT)#其实就是对数组进行计算
    #print tfidf
    print 'i finish transforming tfidf'
    #获取词袋模型中的所有词语
    word = freWord.get_feature_names()#获取词袋模型中的所有词语
    print '特征维度：',len(word),datetime.datetime.now()
    #输出特征词
    #for i in word:
    #    print i
    #得到权重
    #weight = tfidf.toarray()#将tf-idf矩阵取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
    
    '''#写入文件
    '''
    output = 'ZTZ_trainforsogou_age.txt'
    with open(output,'w') as w:
        for i in range(0,len(dataList)):
            w.write('%s %s\n' % (label[i],''.join(' {0}:{1}'.format(f,tfidf[i,f]) for f in sorted(tfidf[i].nonzero()[1]))))
    
    print 'finish writing train',datetime.datetime.now()     
    
    print '训练集第一行tfidf特征'
    print tfidf[0]
    idxofNZ = sorted(tfidf[0].nonzero()[1])
    print idxofNZ
    for i in idxofNZ:
        print tfidf[0,i]
    '''

    '''
    testsen = '首页 英雄'
    testsenlist = []
    testsenlist.append(testsen.decode('utf8'))

    print freWord.transform(testsenlist).toarray()

    result = transformer.transform(freWord.transform(testsenlist).toarray())
    print result
    print result.toarray()
    '''
    
    '''
    print 'start training'
    #X = [[0, 0], [1, 1]] 
    #y = [5, 1] #必须要是整数或者字符串
    clf = svm.SVC() 
    #print weight.shape[1],weight.shape[0]
    clf.fit(weight, label) 
    #result = clf.predict(result.toarray()) 
    #print result[0]
    print 'finish training'
    
 
    
    #最后输出
    finalresult = []
    for line in lines:
        temp = []
        #here!cut的形式
        #两个cut须一致，上面还有一个cut
        for i in jieba.cut(line,cut_all=True):
            if i not in stopwords:
                if i not in blanklist:
                    temp.append(i)
        fo = ' '.join(temp)
        #print fo
        #print type(fo)#unicode
        testsenlist = []
        testsenlist.append(fo)
        print fo
        result = transformer.transform(freWord.transform(testsenlist).toarray())
        print result
        print result.shape[1]
        predResult = clf.predict(result.toarray())
        #print predResult[0]
        finalresult.append(predResult[0])
    #print finalresult
    S = '\n'.join(str(i) for i in finalresult)
    #here!改变输出结果
    open(r'result_of_newSogou.txt','w').write(S)

  
    #to test files
    #here!打开test集
    f = open(r'F:\study\master of TJU\DF\Sogou\DF-competition-sogou\data\testing_data_final.txt','r')
    lines = f.readlines()
    print '测试集维度',len(lines)
    print datetime.datetime.now()    
    output = 'ZTZ_testforsogou_age.txt'
    testdata = open(output,'w')

    for line in lines:
        #print 1
        temp = []
        for i in jieba.cut(line,cut_all=False):
            if i not in stopwords:
                if i not in blanklist:
                    if i in corpus:
                        temp.append(i)     
        fo = ' '.join(temp) 
        #print fo
        testsenlist = []
        testsenlist.append(fo)
        result = transformer.transform(freWord.transform(testsenlist))
        #print result
        testdata.write('%s %s\n' % ('1',''.join(' {0}:{1}'.format(f,result[0,f]) for f in sorted(result[0].nonzero()[1]))))
    print 'finish reading,start training',datetime.datetime.now()
    sleep(45)
    '''
    #here 
    y,x = svm_read_problem('ZTZ_trainforsogou_age.txt')
    yt,xt = svm_read_problem('ZTZ_testforsogou_age.txt')
    model = svm_train(y,x,'-c 20 -h 0')
    p_label,p_acc,p_val = svm_predict(yt,xt,model)
    print len(p_label),'finish'


    
    