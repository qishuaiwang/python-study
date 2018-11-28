#!/usr/bin/env python
#coding=utf-8


'''
test_str = "How old    are you?"
test_lst = test_str.split()
#test_lst.extend(test_str)
result_str = " ".join(test_lst)
print(result_str)
'''

string = "I love  code."        #code 前有两个空格
print(string)

str_lst =string.split(" ")      #以空格分隔字符串
print(str_lst)

words = [s for s in str_lst if s!='']      #利用列表解析，将空字符删除，空格为分隔符，产生了一个空字符
print(words)

new_string = " ".join(words)
print(new_string)
