#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第三十一题

print 'you enter a dark room with two door. do you go through door #1 or door #2'
door=raw_input(">")
#选择进入第一扇门
if door=='1':
    print 'there is a giant bear hear here eating a cheese cake.what do you do?'
    print '1.take the cake '
    print '2 scream at the bear'
    #今入第一扇门后的选择
    bear=raw_input('>')
    if bear=='1':
        print 'the bear eats your face off.good job'
    elif bear=='2':
        print  'the brar eats your legs off,good job'
    else:
        print 'well,doing %s is probably better.bear runs away.' %bear
elif door=='2':
    print 'you stare into the endless abyss at Cthuhu is retina'
    print '1.bluebarries'
    print '2 yellow jacket clothspins'
    print '3.understanding revolvers yelling melodies'
    insanity=raw_input('>')
    if insanity=='1' or insanity=='2':
        print 'your body survives powered by a mind of jello,goog job'
    else:
        print 'the insanity rots your eyes into a poll of muck.good jobs'
else:
      print 'you stumble around and fall on a knief and die.good job!'