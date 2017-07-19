#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第十六题
#文件的相关操作
from sys import argv
script,file_name=argv
print 'the read of file name is %s' %file_name
#打开一个文件
file=open(file_name,'rw+')
print '''
文件操作的命令:
1.close – 关闭文件。跟你编辑器的 文件->保存.. 一个意思。
2.read – 读取文件内容。你可以把结果赋给一个变量。
3.readline – 读取文本文件中的一行。
4.truncate – 清空文件,请小心使用该命令。
5.write(stuff) – 将 stuff 写入文件。
'''
#打印文件内容
print file.read()
#由于文件在读取文件之后指针已经在文章的最后了,在清空文档是不成功的.
#移动指针位置
file.seek(0,0)
#清空文件内容
file.truncate()
#对该文件进行写操作
file.write('line1\n')
file.write('line2\n')
file.write('line3\n')
#返回文章当前位置
print file.tell()
#读取文件内容
file.seek(0,0)
#返回文章当前位置
print file.tell()
print file.read()
#关闭文件
file.close()
