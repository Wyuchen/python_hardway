#!/usr/bin/python
#coding=utf-8
# 笨办法学 Python-第二十四题
#针对前面的知识的复习和总结

print 'let us practice everything'

print 'you\'d need to konw \'bout escapes with \\ that do \n newline and \t tabs'

poem='''
\tThe Zen of Python, by Tim Peters\n
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

print '==================================='
print poem
print '==================================='

five=10-2+3-6
print 'this should be five: %d'  %five

def secret_formula(started):
    jelly_beans=started*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates
start_point=1000
beans,jars,crates=secret_formula(start_point)

print 'with a starting point of : %d' %start_point
print 'we have %d beans,%d jars, and %d crates.'%(beans,jars,crates)

start_point/=10
print 'we have %d beans,%d jars, and %d crates.' %secret_formula(start_point)
