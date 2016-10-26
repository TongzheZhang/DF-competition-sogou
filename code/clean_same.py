#-*- coding: utf-8 -*-
import pandas as pd

inputfile = '../data/1.csv' #评论文件user_tag_query.2W.TRAIN
outputfile = '../data/unique.csv' #评论处理后保存路径
data = pd.read_csv(inputfile, header = None)
l1 = len(data)
data = pd.DataFrame(data[0].unique())
l2 = len(data)
data.to_csv(outputfile, index = False, header = False)
print(u'删除了%s条评论。' %(l1 - l2))