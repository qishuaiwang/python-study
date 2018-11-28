#! /usr/bin/env python
#coding=utf-8

'''
for i in range(1,100):
    if (not(i%3)):
        print (i, end = ' ')
'''

aliquot = []
for n in range(1,100):
    if (0 == (n%3)):
        aliquot.append(n)
print(type (aliquot))
print (aliquot)
s_t = str(aliquot)
print(type (s_t))
print (s_t)
s_t_s = s_t.split(",")
print(type (s_t_s))
print (s_t_s)
print ("".join(s_t_s))
