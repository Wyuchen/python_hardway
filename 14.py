#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第十四题
#raw_input & 传递参数

from sys import argv
script,user_name,sex =argv
prompt='#>'
print 'hi %s,i am the %s script' %(user_name,script)
print 'i would like to ask you a few questions'
print 'do you like me, %s' % user_name
likes=raw_input(prompt)

print 'where do you live, %s' % user_name
lives=raw_input(prompt)

print 'what kind of computer do you have?'
computer=raw_input(prompt)

print 'you are %s,what kind of game do you like?' %sex
gamename=raw_input(prompt)

print '''
alright,so you said %r about liking me.
you live in %r. not sure where that is.
and you have a %r computer.nice
and you like %r game.
''' %(likes,lives,computer,gamename)