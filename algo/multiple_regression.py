#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/25 3:20 下午
# @File    : multiple_regression.py
# @author  : Akaya
# @Software: PyCharm
# multiple_regression  :

import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

# 预测重量为 2300kg、排量为 1300ccm 的汽车的二氧化碳排放量：

predictedCO2 = regr.predict([[2300, 1300]])

print(regr.coef_)
print(predictedCO2)
