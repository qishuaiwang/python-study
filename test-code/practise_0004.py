#!/usr/bin/env python
#coding=utf-8
'''
loop_n = 4
s_lst = [0, 1]
r_lst = [0, 1]
for i in range(2,(loop_n + 1)):
    r_lst.append((r_lst[i-1] + r_lst[i-2]))
print(r_lst[loop_n])
'''

a, b = 0, 1

for i in range(2):
    a, b = b, a+b

print(a)
