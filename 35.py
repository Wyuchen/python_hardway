#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第三十五题
from sys import exit
def gold_room():
    print 'the rom is full of gold.how much do you take?'
    next=raw_input('>')
    if '0' in next or 'i' in next:
        how_much=int(next)
    else:
        dead('man,lean to type a number.')
    if how_much <50:
        print "nice,you are not greedy,you win"
        exit(0)
    else:
        dead('you greedy bastard!')

def bear_room():
    print 'there is a bear here.'
    print 'the bear has a bunch of honey,熊有一堆蜂蜜'
    print 'the fat bear is in front of another door,胖熊在另一个门前'
    print 'you can choose take honey or taunt bear or taunt bear twice '
    bear_moved=False
    while True:
        next=raw_input(">")
        if next =="take honey":
            dead('the bear looks at you then slaps you face off,熊看着你然后拍打你的脸')
        elif next=='taunt bear' and not bear_moved:
            print 'the bear has moved from the door,you can go through it now'
            bear_moved=True
        elif next=='taunt bear twice' and  bear_moved:
            dead('the bear gets pissed off and chews your leg off,熊生气了，咬了你的腿')
        elif next=="open door" and bear_moved:
            gold_room()
        else:
            print 'i got no idea what that mean'

def cthulhu_room():
    print 'here you see the great evil cthulhu,这里你看到伟大的邪恶的恶魔'
    print 'he,it,whatever stares at you and you go insane,他把你盯毛了'
    print 'do you flee for your life or eat your head?,你是逃避生命还是自杀'
    next=raw_input(">")
    if 'flee' in next:
        start()
    elif 'head' in next:
        dead('well that was tasty,这很可口!')
    else:
        cthulhu_room()

def dead(why):
    print why,'good job'
    exit(0)

def start():
    print 'you are in dark room'
    print 'there is a door to your right and left'
    print 'which one do you take?'

    next=raw_input('>')
    if next=="left":
        bear_room()
    elif next=="right":
        cthulhu_room()
    else:
        dead('you stumble around the romm until you starve,你跌倒在房间里直到你饿死')

start()