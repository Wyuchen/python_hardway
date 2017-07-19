#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第四十题
#字典的学习
cities={'ca':'CA','mi':'MI','fl':'FL'}
cities['ny']='NY'
cities['or']='OR'
def find_city(list,key):
    if key in list:
        return list[key]
    else:
        return 'not found'
cities['_find']=find_city #将函数名赋值到列表中
#遍利列表中的key和valus值
for key in cities:
    print key
    print cities[key]

print cities
while True:
    print 'state?(enter to quit)',
    key=raw_input('> ')
    if not key: break
    city_found=cities['_find'](cities,key)
    print city_found

