#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:23:11 2018

@author: patrickorourke
"""
import numpy as np
import matplotlib.pyplot as plt

w = open('/Users/patrickorourke/documents/time_without.txt', 'r')
without = np.array(w.readlines())
w.close()

b = open('/Users/patrickorourke/documents/time_batching.txt', 'r')
batching = b.readlines()
b.close()

t= open('/Users/patrickorourke/documents/time_ten.txt', 'r')
ten = t.readlines()
t.close()

without = [float(i.rstrip()) for i in without]

batching = [float(i.rstrip()) for i in batching]

ten = [float(i.rstrip()) for i in ten]

plt.plot(without, label = "Time without Deep-Learning Libaries")
plt.plot(ten, label = "Time with TensorFlow")
plt.plot(batching, label = "Time with Batching")
plt.title('Execution time ')
plt.xlabel("Epochs")
plt.ylabel("Time")
plt.legend()