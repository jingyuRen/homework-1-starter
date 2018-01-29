#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 21:20:57 2018

@author: albertzhang
"""
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_boston

boston_data = load_boston()
data = boston_data['data']
target = boston_data['target']
fig, axes = plt.subplots(3, 5, figsize = (15, 10))
for i in range (0,5):
    axes[0,i].scatter(data[:,i], target,marker='+',color='b', alpha=0.3)
for i in range (0,5):
    axes[1,i].scatter(data[:,5 + i], target,marker='+',color='b', alpha=0.3)
for i in range (0,3):
    axes[2,i].scatter(data[:,10 + i], target,marker='+',color='b',alpha=0.3)
axes[0,0].set_xlabel('CRIM')
axes[0,0].set_ylabel('MEVD')
axes[0,1].set_xlabel('ZN')
axes[0,2].set_xlabel('INDUS')
axes[0,3].set_xlabel('CHAS')
axes[0,4].set_xlabel('NOX')
axes[1,0].set_xlabel('RM')
axes[1,0].set_ylabel('MEVD')
axes[1,1].set_xlabel('AGE')
axes[1,2].set_xlabel('DIS')
axes[1,3].set_xlabel('RAD')
axes[1,4].set_xlabel('TAX')
axes[2,0].set_xlabel('PTRATIO')
axes[2,0].set_ylabel('MEVD')
axes[2,1].set_xlabel('B')
axes[2,2].set_xlabel('LSTAT')
axes[2][3].axis('off')
axes[2][4].axis('off')
plt.suptitle('Graph of feature against MEVD')
plt.savefig('/Users/jingyu/Desktop/Spring 2018/Applied Machine Learning/homework-1-jingyuRen/task3/task33.png')
plt.show()
