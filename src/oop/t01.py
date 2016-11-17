# -*- coding:utf-8 -*-  
'''
Created on 2016年11月17日
@author: zhaodj 

这个类用来练习python的oop
'''

class News(object):
    def __init__(self, title, update_time):
        self.__title = title
        self.__update_time = update_time

    def News_Info(self):
        print(self.__update_time,'\t', self.__title)

news = News('上海已值深秋，今天飘起了小雨','2016-11-17 12:44:15')
news.News_Info()