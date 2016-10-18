# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:25:58 2016

@author: chenyao
"""

import pandas as pd

inputfile = '../data/age.csv' #评论文件
outputfile = '../data/age2.csv' #评论处理后保存路径
data = pd.read_csv(inputfile) #读入数据
data['age'] = [bin(i)[2:] for i in data['age']]#十进制转换二进制
#print (data['age'])
data.to_csv(outputfile) #输出结果，写入文件

