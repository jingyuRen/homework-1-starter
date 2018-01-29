#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 02:52:22 2018

@author: jingyu
"""

from __future__ import division
import numpy as np


def test_one():
    assert 2/8 == 0.25
def test_two():
    assert np.array([2])/np.array([8]) == 0.25