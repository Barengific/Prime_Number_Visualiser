# -*- coding: utf-8 -*-
"""

@author: barengific
"""
import numpy as np
import matplotlib.pyplot as plt

arr = np.array([])
x = np.array([])

for i in range(1, 1000000):   
    #print(i)
    
    a = (i//2)
    b = a+1
    #print(i,"here",a)
    for j in range(2, b):
        #print("aaaaa")
        #print(j)
        #print("-----")
        if i%j==0:
            #print(i, "not prime")
            break
        elif i%j!=0:
            #print(i, " not div ", j)
            1+1
        if j == a:
            #print("TRUE PRIME",i)
            z = np.array([i])
            arr = np.concatenate((arr, z))
            #print(arr)
            q = np.array([i])
            x = np.concatenate((x, q))
            
print(arr)      
#zz = np.array([6,6,6,6,6,6,6,6,6])      
#arra = np.concatenate((arra, zz))
#print(arra)
print(x)

plt.plot(arr)
plt.ylabel('some numbers')
plt.show()