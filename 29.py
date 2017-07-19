#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第二十九题
#条件判断语句if
people=20
cats=30
dogs=15

if people < cats:
    print 'too many cats!too little people'
if people > cats:
    print 'too many people,too little cats'
if people < dogs:
    print 'the world is drooled on'
if people > dogs:
    print 'the world is dry'

dogs+=5

if people >dogs:
    print 'people > dogs'
if people <dogs:
    print 'people <dogs'
if people == dogs:
    print 'people are dogs'