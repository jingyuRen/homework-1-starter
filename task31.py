#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 05:23:16 2018

@author: jingyu
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


bedcheet=pd.read_csv('/Users/jingyu/Desktop/Spring 2018/Applied Machine Learning/homework-1-jingyuRen/task3/bedsheet.csv')
cheese=pd.read_csv('/Users/jingyu/Desktop/Spring 2018/Applied Machine Learning/homework-1-jingyuRen/task3/cheese.csv')
year = bedcheet['Years'].tolist()
years = np.array(year)
beddata = bedcheet['Bedsheet tanglings'].tolist()
bedarray = np.array(beddata)
cheesedata = cheese['cheese consumed'].tolist()
cheesearray = np.array(cheesedata)
plt.figure(figsize=(11,3))
ax1 = plt.gca()
line1, = ax1.plot(years,cheesearray,'o-',c='r')
ax2 = ax1.twinx()
line2, = ax2.plot(years,bedarray,'o-',c='k')
plt.legend((line1,line2),('cheese consumed','bedcheet tanglings'))
ax1.set_ylabel('cheese consumed(lbs)')
ax1.set_ylim([28.5,34.5])
ax2.set_ylabel('bedcheet tanglings(deaths)')
ax2.set_ylim([200,1000])
plt.title('Number of people who died by becoming tangled in their bedcheets' )

plt.savefig('/Users/jingyu/Desktop/Spring 2018/Applied Machine Learning/homework-1-jingyuRen/task3/task31.png')

plt.show()
