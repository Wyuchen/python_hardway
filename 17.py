#!/usr/bin/python
#coding=utf-8
# 笨办法学 Python-第十七题
#通过文件操作对文件进行复制
from sys import argv
import os
from os.path import exists
# 给出文件的名称
script,from_file,to_file=argv
print 'coping from %s to %s' %(from_file,to_file)
#打开要复制的文件
Ffile=open('./15_sample.txt')
#读取要复制的文件
indata=Ffile.read()
#查看复制内容的长度
print "the input file is %d bytes long " % len(indata)
#判断是否有这个文件
print "dose the output file exits %r" %exists(to_file)

Tfile = open(to_file, 'w+')

#写入要复制的内容
Tfile.write(indata)
# 关闭文件
Tfile.close()
Ffile.close()


