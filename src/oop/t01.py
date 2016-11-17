# -*- coding:utf-8 -*-  
'''
Created on 2016年11月17日
@author: zhaodj 

这个类用来练习python的oop
'''

class News(object):
    def __init__(self, title, update_time):
        #第一个参数self，代指实例本身
        #变量前加双下划綫，表示属性封装，对外部不可见
        self.__title = title
        self.__update_time = update_time

    def News_Info(self):
        print(self.__update_time,'\t', self.__title)
    
    #让外部代码通过类自己提供的方法，来访问属性 getter setter
    def get_title(self):
        return self.__title
    def set_title(self,title):
        self.__title = title

news = News('上海已值深秋，今天飘起了小雨','2016-11-17 12:44:15')
news.News_Info()
#调用News类自己提供的方法，访问title属性
title = '道狭草木长，夕露沾我衣，衣沾不足惜，但使愿无违'
print('调用set方法：',news.set_title(title))
print('调用get方法：',news.get_title())

print('****************')
#继承、多态
class Animal(object):
    def run(self):
        print('父类的run方法ing')
class Dog(Animal):
    def __init__(self):
        pass
    def run(self):
        print('dog类的run方法')
dog = Dog()
dog.run()
ass = list()
#判断实例对象 isinstance：list,set,dict,tuple,str,Object
print(isinstance(ass, Animal))
print(isinstance(news, News))
#dog是Animal类型吗
print(isinstance(dog, Animal))
print(isinstance(dog, Dog))