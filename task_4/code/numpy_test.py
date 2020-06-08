# -*-coding:utf-8 -*-
# @Time:2020/5/16 20:38
# @Author:CHM
# @File:numpy_test.py
import numpy as np

"""一.创建数组"""
# 1.创建一维数组对象
array_ = np.array([1, 2, 3])
list_ = [1, 2, 3]
print(array_)

# 2.创建二维数组对象
array_ = np.array([[1, 2], [3, 4]])
print(array_)

# 3.np.empty
x = np.empty((3, 2), dtype=np.int)
print(x)

# 4.np.zeros
x = np.zeros(5)
print(x)
x = np.zeros((3, 4))
print(x)

# 5.np.ones
x = np.ones(5)
print(x)
x = np.ones((2, 2), dtype=np.int)
print(x)

"""二.ndarray属性"""
# 1. ndarray.ndim 秩，即轴的数量或维度的数量
print(x.ndim)

# 2. ndarray.shape 数组的维度，对于矩阵，n行m列
print(x.shape)

# 3.ndarray.size 数组元素的总个数，相当于 .shape 中 n*m 的值
print(x.size)

"""三.从已有数组创建数组"""

# 1.将列表转为ndarray
x = [1, 2, 3]
y = np.asarray(x)
print(y)
x = [[1, 2], [3, 4], [5, 6]]
y = np.asarray(x)
print(y)

# 2.创建shape相同的ndarray
x = [[1, 2], [3, 4], [5, 6]]
y = np.ones_like(x)
print(y)
y = np.full_like(x, 2)
print(y)
y = np.zeros_like(x)
print(y)
y = np.empty_like(x)
print(y)

"""四.从数值范围创建数组"""
# 1. arrange
x = np.arange(0, 10, 1)
print(x)

# 2. linspace
x = np.linspace(1, 10, 10)
print(x)

# 3. reshape
x = np.linspace(1, 10, 10).reshape((2, 5))
print(x)

"""五.切片和索引"""
# 1.切片
a = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
print(a[1:])
print(a[:, 1:])
print(a[..., 1:])
print(a[1, 1:])
print(a[1:, 2])
print(a[..., 2])

# 2.索引
print(a[0, 0])
print(a[2, 2])

# 3. 高级索引1
x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 0]]
print(y)

# 4. 高级索引2
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print(y)

# 5. 高级索引3
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a = x[1:3, 1:3]
b = x[1:3, [1, 2]]
c = x[..., 1:]
print(a)
print(b)
print(c)

# 6. 布尔索引
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x[x > 5])
a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(a[~np.isnan(a)])

# 7. 花式索引
x = np.arange(32).reshape((8, 4))
print(x)
print(x[[5, 2, 4, 7]])

"""六.Numpy广播"""
# 1. 维度相同
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a*b
print(c)

# 2. 维度不一样
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
print(a + b)

# 3. 维度不一样，具体实现
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
bb = np.tile(b, (4, 1))  # 重复 b 的各个维度
print(a + bb)

"""七.迭代数组"""
a = np.arange(6).reshape(2,3)
for x in np.nditer(a):
    print (x, end=", ")

"""八.数组操作"""
# 1. 修改数组形状
a = np.arange(8)
b = a.reshape((4,2))
print(b)
for row in b:
    print(row)
for element in a.flat:
    print(element)
# order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
print(b.flatten())
print(b)
print(b.ravel(order="F"))
# 2. 翻转数组
a = np.arange(12).reshape((3,4))
print(a)
print(np.transpose(a))
print(a.T)
# 3. 修改数组维度
x = np.array([[1],[2],[3]])
y = np.array([4,5,6])
b = np.broadcast(x,y)
print(b)
# r,c = b.iters
# print(next(r),next(c))
# print(next(r),next(c))
# print(next(r),next(c))
c = np.empty(b.shape)
c.flat = [u+v for (u,v) in b]
print(c)
print(x+y)

a = np.arange(4).reshape((1,4))
print(np.broadcast_to(a,(4,4)))
# np.expand_dims
x = np.array([[1,2],[3,4]])
y = np.expand_dims(x,axis=0)
print(y)
y = np.expand_dims(x,axis=1)
print(y)
# numpy.squeeze
x = np.arange(9).reshape(1,3,3)
y = np.squeeze(x)
y = np.squeeze(y)
print(y.shape)
# 4. 连接数组
# np.concatenate
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(np.concatenate((a,b)))
print(np.concatenate((a,b),axis=1))
# np.stack
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(np.stack((a,b)))
print(np.stack((a,b),axis=1))
# np.hstack
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c = np.hstack((a,b))
d = np.vstack((a,b))
print(c)
print(d)
# 5. 分割数组
a = np.arange(9)
b = np.split(a,3)
c = np.split(a,[4,7])
print(b)
print(c)
# 6. 数组元素的添加与删除
a = np.array([[1,2,3],[4,5,6]])
print (np.append(a, [7,8,9]))
print (np.append(a, [[7,8,9]],axis = 0))
print (np.append(a, [[5,5,5],[7,8,9]],axis = 1))
"""九.数学函数 """
a = np.array([0,30,45,60,90])
print ('不同角度的正弦值：')
# 通过乘 pi/180 转化为弧度
print(np.sin(a*np.pi/180))

a = np.array([1.0,5.55,  123.4,  0.567,  25.532])
print(np.around(a))

a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
print(np.floor(a))

a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
print(np.ceil(a))

"""十.算术运算"""
a = np.arange(9, dtype = np.float_).reshape(3,3)
print(a)
b = np.array([10,10,10])
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))

a = np.array([10,100,1000])
print (np.power(a,2))
b = np.array([1,2,3])
print (np.power(a,b))

a = np.array([10,20,30])
b = np.array([3,5,7])
print (np.mod(a,b))
print (np.remainder(a,b))

"""十一.统计函数"""
a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print(a)
print(np.min(a))
print (np.amin(a,1))
print (np.amin(a,0))
print (np.amax(a))
print (np.amax(a, axis = 0))

a = np.array([[30,65,70],[80,95,10],[50,90,60]])
print(np.median(a))
print(np.median(a, axis =  0))
print(np.median(a, axis =  1))

print(np.mean(a))
print(np.mean(a, axis =  0))
print(np.mean(a, axis =  1))

print(np.average(a))
print(np.average(a, axis =  0))
print(np.average(a, axis =  1))

print(np.std(a))
print(np.std(a, axis =  0))
print(np.std(a, axis =  1))

"""十二.排序、条件筛选"""
print(np.sort(a,kind='quicksort'))
print(np.sort(a, axis = 0))
print(np.sort(a, axis = 1))
dt = np.dtype([('name',  'S10'),('age',  int)])
a = np.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)], dtype = dt)
print (np.sort(a, order =  'age'))

a = np.array([[30,40,70],[80,20,10],[50,90,60]])
print (np.argmax(a,axis=1))
print (a.flatten())
maxindex = np.argmax(a, axis =  0)
maxindex = np.argmax(a, axis =  1)
minindex = np.argmin(a)
print (a.flatten()[minindex])
minindex = np.argmin(a, axis =  0)
minindex = np.argmin(a, axis =  1)

x = np.arange(9.).reshape(3,  3)
print(x)
y = np.where(x > 3)
print (y)
print (x[y])

"""十三.线性代数"""
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
print(np.dot(a,b))

a = [[1,2],[3,4]]
b = [[11,12],[13,14]]
print (np.matmul(a,b))

"""十四.io"""
a = np.array([1, 2, 3, 4, 5])
# 保存到 outfile.npy 文件上
np.save('outfile.npy', a)
b = np.load('outfile.npy')
print (b)