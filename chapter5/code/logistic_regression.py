#-*- coding: utf-8 -*-
#逻辑回归 自动建模
import pandas as pd

#参数初始化
filename = '../data/bankloan.xls'
data = pd.read_excel(filename)
x = data.iloc[:,:8].as_matrix()
y = data.iloc[:,8].as_matrix()

from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR 
rlr = RLR() #建立随机逻辑回归模型，筛选变量
rlr.fit(x, y) #训练模型
rlr.get_support() #获取特征筛选结果，也可以通过.scores_方法获取各个特征的分数
print(u'通过随机逻辑回归模型筛选特征结束。')
print(u'有效特征为：%s' % ','.join(data.iloc[:,:8].columns[rlr.get_support()]))
x = data.iloc[:,:8][data.iloc[:,:8].columns[rlr.get_support()]].as_matrix() #筛选好特征

lr = LR()
lr.fit(x,y)
print(u'逻辑回归模型训练结束')
print(u'模型的平均正确率为：%s' %lr.score(x,y))