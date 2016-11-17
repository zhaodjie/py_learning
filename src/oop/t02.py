# -*- coding:utf-8 -*-

'''
 type()方法
'''
#from oop.t01 import news

print(type(1123))
print(type(x for x in range(1,10)))  #生成器generator
print(type([1,44,15])) # list
print(type('str'))
print(type(None)) # NoneType
print(type(object)) #返回了 'type'
print(type(abs)) #如果一个变量指向了函数或者类,也可用type()函数判断
#print(type(news)) #导入另一个py文件中的类，使用type()函数判断