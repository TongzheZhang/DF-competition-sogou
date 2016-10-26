# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:00:10 2016

@author: chenyao
"""


import pandas as pd
import jieba #导入结巴分词，需要自行下载安装

#参数初始化
inputfile1 = '../data/temp.txt'
#inputfile2 = '../data/meidi_jd_pos.txt'
outputfile1 = '../data/temp_cut.txt'
#outputfile2 = '../data/meidi_jd_pos_cut.txt'

data1 = pd.read_csv(inputfile1, header = None) #读入数据
#print (data1)
#data2 = pd.read_csv(inputfile2, encoding = 'utf-8', header = None)
mycut = lambda s: ' '.join(jieba.cut(s)) #自定义简单分词函数
data1 = data1[0].apply(mycut) #通过“广播”形式分词，加快速度。
print (data1)
data1.to_csv(outputfile1, index = False, header = False, encoding = 'utf-8') #保存结果
#data2.to_csv(outputfile2, index = False, header = False, encoding = 'utf-8')