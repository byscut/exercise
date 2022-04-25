#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/25 3:29 下午
# @File    : train_test.py
# @author  : Akaya
# @Software: PyCharm
# train_test  :  https://www.w3school.com.cn/python/python_ml_train_test.asp

import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()


r2 = r2_score(train_y, mymodel(train_x))
print(r2)

r2 = r2_score(test_y, mymodel(test_x))
print(r2)

print(mymodel(5))
