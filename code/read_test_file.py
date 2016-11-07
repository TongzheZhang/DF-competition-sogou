# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:09:50 2016


读取测试集，逐行输出结果。
@author: Richard

"""
f = open(r"F:\\study\master of TJU\DF\Sogou\DF-competition-sogou\data\final_by_shi\testing_data_test.txt")  
lines = f.readlines()#读取全部内容  
#print lines
for line in lines:
    print line  