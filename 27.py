#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第二十七题
#逻辑运算关系
print '''
逻辑术语:
and  与
or   或
not  非
!=   不等于
==   等于
>=   大于等于
<=   小于等于
True 真
False 假
'''

print '真值表:'
print '''

NOT        True?

not False  True
not True   False

OR             True?

True or False  True
True or True   True
False or True  True
False or False False

AND             True?

True and False  False
True and True   True
False and True  False
False and False False

NOT OR               True?

not (True or False)  False
not (True or True)   False
not (False or True)  False
not (False or False) True

NOT AND               True?

not (True and False)  True
not (True and True)   False
not (False and True)  True
not (False and False) True

!=     True?

1 != 0 True
1 != 1 False
0 != 1 True
0 != 0 False

==     True?

1 == 0 False
1 == 1 True
0 == 1 False
0 == 0 True
'''