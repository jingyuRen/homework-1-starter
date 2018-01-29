#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 06:54:32 2018

@author: jingyu
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris 

iris_dataset = load_iris()

setosa = iris_dataset['data'][iris_dataset['target'] == 0]
versicolor = iris_dataset['data'][iris_dataset['target'] == 1]
virginica = iris_dataset['data'][iris_dataset['target'] == 2]

fig, axes = plt.subplots(4,4,figsize=(15,15))

for i in range(0,4):
    for j in range(0,4):
        if i == j:
            axes[i,j].hist(np.append(np.append(setosa[:,i],versicolor[:,i]),virginica[:,i]),bins=20)
for i in range(0,4):
    for j in range(0,4):
        if i != j:   
            axes[j,i].scatter(setosa[:,i], setosa[:,j])
            axes[j,i].scatter(versicolor[:,i], versicolor[:,j])
            axes[j,i].scatter(virginica[:,i], virginica[:,j])
            axes[j,i].legend(('setosa','versicolor','virginica'))
for i in range(0,4):
    axes[i,0].set_xlabel('sepal length(cm)')
for i in range(0,4):
    axes[i,1].set_xlabel('sepal width(cm)')
for i in range (0,4):
    axes[i,2].set_xlabel('petal length(cm)')
for i in range (0,4):
    axes[i,3].set_xlabel('petal width(cm)')
    
for j in range(0,4):
    axes[0,j].set_ylabel('sepal length(cm)')
for i in range(0,4):
    axes[1,j].set_ylabel('sepal width(cm)')
for i in range (0,4):
    axes[2,j].set_ylabel('petal length(cm)')
for i in range (0,4):
    axes[3,j].set_ylabel('petal width(cm)')

plt.savefig('/Users/jingyu/Desktop/Spring 2018/Applied Machine Learning/homework-1-jingyuRen/task3/task32.png')
plt.show()
