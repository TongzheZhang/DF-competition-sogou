# DF-competition-sogou
大数据精准营销中搜狗用户画像挖掘

我们将对数据训练集和测试集进行中文语义分析，特征值提取，分类模型拟合和预测等步骤操作。
数据库：user_tag_query.2W.TEST user_tag_query.2W.TRAIN
具体处理流程：
1. 文本预处理
2. 特征提取
3. 训练分类器
4. 模型预测


结果：

去除停用词之前：

正常结果bigram+truecut 0.66117

使用unigram+truecut 0.6509

使用bigram+searchcut 0.6633

使用unigram+searchcut 0.6566

使用bigram+falsecut 0.66546

使用unigram+falsecut 0.65675



在去除停止词之后：

正常结果bigram+truecut 0.6625

uni_truecut 0.64879

bigram+falsecut 0.66625

uni_cutfalse 0.65158

bi_searchcut 0.66596

uni_searchcut 0.65308

libsvm：



c = 0.5，预测值一样。放弃

c = 1 预测值的四分之三是一致的，所以放弃

c = 4：0.62913 预测值少了一些少数类，多数类比重加大。 

c = 10：0.65254

c = 20 0.64746 心好累

c = 30 age预测值都是一，放弃。

c = 50：age预测值都是一，放弃。

bigram：c = 1 ：大约需要两个半小时，放弃。


after corpus：

c = 20：edu全都是5，舍弃

c = 30：age全都是1，舍弃


我们提交14次。

最高分 0.70162 提交次数 60次。