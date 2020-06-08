# -*-coding:utf-8 -*-
# @Time:2020/5/16 15:47
# @Author:CHM
# @File:KNN.py
from numpy import *
import operator


def createDataSet():
    # 创建训练集
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

# np.tile
def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    # 根据欧式距离计算训练集中每个样本到测试点的距离
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    # 计算完所有点的距离后，对数据按照从小到大的次序排序
    sortedDistIndicies = distances.argsort()
    # 确定前k个距离最小的元素所在的主要分类，最后返回发生频率最高的元素类别
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

x,y = createDataSet()
result  = classify([0.1,0],x,y,3)
print(result)