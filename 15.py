#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第十五题
#通过变量获取读取文件名称,文件的相关操作
from sys import argv
script,file_name=argv
print 'the read of file name is %s' %file_name
#打开一个文件
file=open(file_name,'rb+')
#打印文件内容
print file.read()
#关闭文件
file.close()
#获取另外一个文件
file_name1=raw_input("please input other file_name >")
#打开一个文件
file1=open(file_name1,'rb+')
#打印文件内容-一行
print  file1.readline()
#关闭文件
file1.close()
