# -*-coding:utf-8 -*-
# @Time:2020/5/22 20:52
# @Author:CHM
# @File:matplotlib_test.py
from matplotlib import pyplot as plt
import numpy as np
plt.plot([1,3,5,2,6,3])
plt.show()

x = np.linspace(-2*np.pi,2*np.pi,1000)
y = np.sin(x)
plt.plot(x,y)
plt.show()

x = np.linspace(-2*np.pi,2*np.pi,10)
y = np.sin(x)
plt.bar(x,y)
plt.show()

x = np.random.normal(0,1,100)
y = np.random.normal(0,1,100)
plt.scatter(x,y)
plt.show()

x = [1,2,3,4,5]
plt.pie(x)
plt.show()

x = np.linspace(-5,5,500)
y = np.linspace(-5,5,500)
X,Y = np.meshgrid(x,y)
Z = X+Y
plt.contourf(X,Y,Z)
plt.show()