#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 03:22:16 2018

@author: jingyu
"""

from __future__ import unicode_literals

def test_length():
    file = open('/Users/jingyu/Desktop/Spring 2018/Applied Machine Learning/homework-1-jingyuRen/task2/input.txt','rb')
    text = file.readline().strip().decode('utf-8')
    assert len(text) == 6
    