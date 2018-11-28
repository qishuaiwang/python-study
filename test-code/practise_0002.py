#!/usr/bin/env python
#coding=utf-8
'''
import random
r_lst = []
for i in range(40):
    r_lst.append((random.randint(1, 100)))

print (r_lst)
r_lst.sort()
print (r_lst)
r_sum = 0
for i in r_lst:
    r_sum += int(i)
print (r_sum)
r_ave = r_sum/40
print (r_ave)
r_n = 0
for i in r_lst:
    if int(i) > r_ave:
        break
    r_n += 1
print (r_n)

r_lst.reverse()
print (r_lst)
'''

from __future__ import division
import random

score = [random.randint(0,100) for i in range(40)]  #0 到 100 之间，随机得到40个整数，组成列表
print(score)

num = len(score)
sum_score = sum(score)      #对列表中的整数求和
ave_num=sum_score/num       #计算平均数
less_ave = len([i for i in score if i<ave_num])     #将小于平均数的找出来，组成新的列表，并度量该列表的长度
print("the average score is:%.1f" %ave_num)
print("There are %d students less than average." %less_ave)

sorted_score = sorted(score, reverse=True)      #对原列表排序
print(sorted_score)
