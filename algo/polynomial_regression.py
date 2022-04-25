#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/25 2:46 下午
# @File    : polynomial_regression.py
# @author  : Akaya
# @Software: PyCharm
# polynomial_regression  :  
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

print("拟合度：", r2_score(y, mymodel(x)))
