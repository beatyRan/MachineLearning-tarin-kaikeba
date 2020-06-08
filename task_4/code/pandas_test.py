# -*-coding:utf-8 -*-
# @Time:2020/5/22 14:06
# @Author:CHM
# @File:pandas_test.py
import pandas as pd
import numpy as np
"""一.快速入门"""
# """1.对象创建 """
s = pd.Series([1,2,3,4,np.nan,5,6,7])
print(s)
df = pd.DataFrame(np.random.randn(7,4),columns=list('ABCD'))
print(df)
df = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Series([1,4,5,6],dtype='float32'),
                     'C' : np.array([3] * 4,dtype='int32'),
                     'D' : pd.Categorical(["test","train","test","train"]),
                     'E' : 'foo' ,
                     'F' : [1,4,3,2]})
print(df)
# """2.查看数据 """
print(df.head(2))
print(df.tail(2))
print(df.index)
print(df.columns)
print(df.values)
print(df.describe())
print(df.T)
print(df)
print(df.sort_index(axis=0,ascending=False))
print(df.sort_values(by="F"))

# """3.选择区块"""
dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df["A"])
print(df[["A","B"]])
print(df[0:3])
print(df.loc[:,"A":"D"])
print(df.loc["20170102":"20170104",["A","D"]])
print(df.loc["20170102",["A","D"]])

print(df.iloc[3])
print(df.iloc[1:2,0:2])
print(df.iloc[[1,2],[0,2]])
print(df.iloc[:,0:2])
print(df.iloc[0:2,:])
print(df.iloc[1,1])
print(df.iat[1,1])
# 布尔索引
print(df.A>0)
print(df[df.A >0])
print(df>0)
print(df[df >0])

"""二.系列series"""
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s['e'])
print(s[['a','c','d']])
print(s[0])

"""三.数据帧"""
# 1. 列表
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)

#2. 字典
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)
#3. series
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)
#4. 列的添加
df["three"] = pd.Series([10,20,30],index=["a","b","c"])
print(df)
df["four"] = df["one"]+df["three"]
print(df)
del df["four"]
print(df)
print(df.iloc[1])

"""四.基本功能"""
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
df = pd.DataFrame(d)
print(df)
print(df.axes)
print(df.dtypes)
print(df.ndim)
print(df.shape)
print(df.size)
print(df.values)

"""四.描述性统计"""
print(df.sum())
print(df.sum(1))
print(df.mean())
print(df.mean(1))
print(df.std())
print(df.std(1))

"""五.缺失数据"""
d = {'one' : pd.Series([1, np.nan, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)

# 1. 检测缺失值
print(df["one"].isnull())
print(df.isnull())

# 2. 缺少数据的计算，求和时Na被视为0
print(df["one"].sum())

# 3. 清理/填充缺少数据
print(df.fillna(0))
print(df["one"].fillna(df["one"].mean()))
print(df.fillna(method="pad")) # pad 向前填充，bfill 向后填充
print(df.fillna(method="bfill"))

# 4. 丢失缺少的值
print(df)
print(df.dropna())

"""六.分组（groupBy）"""
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
print(df)
# 1. 将数据拆分成组
print(df.groupby("Team").groups)
print(df.groupby(["Team","Year"]).groups)
# 2. 迭代遍历分组
grouped = df.groupby("Year")
for name,group in grouped:
    print("______",name)
    print(group)
    print(group["Points"].mean())
# 3. 聚合
print(grouped["Points"].agg([np.sum,np.mean,np.std]))

# 4. 过滤
print(df.groupby("Team").filter(lambda x:len(x)>=2))

"""七.合并/连接"""
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left,right,on="id")
print(rs)
rs = pd.merge(left,right,on=["id","subject_id"])
print(rs)
# left join
rs = pd.merge(left,right,on="subject_id",how="left")
print(rs)
# right join
rs = pd.merge(left,right,on="subject_id",how="right")
print(rs)
# outer join
rs = pd.merge(left,right,on="subject_id",how="outer")
print(rs)
# inner join
rs = pd.merge(left,right,on="subject_id",how="inner")
print(rs)

"""八.可视化"""
# 折线图
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.rand(10,4), columns=list('ABCD'))
df.plot()
plt.show()
# 条形图
df.plot.bar()
plt.show()

df.plot.bar(stacked=True)
plt.show()

df.plot.barh(stacked=True)
plt.show()

# 直方图
df["A"].plot.hist(bins=40)
plt.show()

# 箱型图
df.plot.box()
plt.show()

# 区域块图形
df.plot.area()
plt.show()

# 散点图
df.plot.scatter(x="A",y="B")
plt.show()

# 饼状图
df["A"].plot.pie(subplots=True)
plt.show()