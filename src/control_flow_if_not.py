#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2014

@author: anroco

How to define a negative if in Python?

¿Cómo definir un if negativo en Python?
'''

#the not operator is use to reverse the logical state, if a condition is true,
#then logical not operator will make it false.

#create a integer
n = 10
print('n=' + str(n))

#uses the not operator to reverse the result of the logical expression
if not n == 100:
    print('the value of n is equal to 100')
else:
    print('the value of n is different from 100')
