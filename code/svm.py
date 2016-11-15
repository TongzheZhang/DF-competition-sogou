# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 21:27:15 2016

@author: Richard
"""
import os
os.chdir(r'F:\study\master of TJU\DF\Sogou\DF-competition-sogou\code')
from svmutil import *

y,x = svm_read_problem('ZTZ_trainforsogou_age.txt')
yt,xt = svm_read_problem('ZTZ_testforsogou_age.txt')
model = svm_train(y,x,'-c 20 -h 0')
p_label,p_acc,p_val = svm_predict(yt,xt,model)
print len(p_label),'finish'

