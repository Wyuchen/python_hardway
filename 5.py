#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第五题
#更多的变量和打印使用格式化字符串的方式

#own info introduct
my_name='yuchen'
my_age=20
my_height=175
my_weight=120
my_addr='北京'
print 'my_name: %s' % my_name
print 'my_age: %d' % my_age
print 'height is %d and weight is %d' %(my_height,my_weight)
print '地址(%%r): %r' % my_addr
print '地址(%%s): %s' % my_addr
#普通的计算
print '普通计算:'
print 'if I add %d,%d,sum=%d' %(my_height,my_weight,(my_height+my_weight))
print '''
python 所有的格式化字符了:
%s    字符串 (采用str()的显示)

%r    字符串 (采用repr()的显示)

%c    单个字符

%b    二进制整数

%d    十进制整数

%i    十进制整数

%o    八进制整数

%x    十六进制整数

%e    指数 (基底写为e)

%E    指数 (基底写为E)

%f    浮点数

%F    浮点数，与上相同

%g    指数(e)或浮点数 (根据显示长度)

%G    指数(E)或浮点数 (根据显示长度)

%%    字符"%"
'''