#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第十三题
#为脚本传递参数,解包,变量
#导入相应的模块argv是所谓的参数变量
from sys import argv
#argv “解包(unpack)”,与其将所有参数放到同一个变量下面,把 argv中的东西解包,将所有的参数依次赋予左边的变量名
script,frist,second,third=argv
print 'the script is called:',script
print 'the frist variable is: ',frist
print 'the second variable is ',second
print 'the third variable is ',third

