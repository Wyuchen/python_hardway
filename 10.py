#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第十题
#转义字符的使用
print '字符串中双引号的转义:'
print "i am 6'2\"tail"
print '字符串中但引号的转义:'
print 'i am 6\'2" tail'

print "\\t 代表tab,\\n 代表回车 \\ 代表 \\"
print '\ti am tabbed in'
print 'i\'m split\non a line'
print  "i'm \\ a \\ cat"
print  '转义序列和格式化字符串放到一起:'
print  '\t this is a %s' % 'dog\n i like that dog'
print  '''
i'll do list:
\t* Cat food
\t* friend
\t* Catnip\n\t* Grass
'''

'''
注释部分:
转移字符有那些:
\(在行尾时)	续行符
\\	反斜杠符号
\'	单引号
\"	双引号
\a	响铃
\b	退格(Backspace)
\e	转义
\000	空
\n	换行
\v	纵向制表符
\t	横向制表符
\r	回车
\f	换页
\other	其它的字符以普通格式输出
'''