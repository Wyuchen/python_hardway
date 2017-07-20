#!/usr/bin/python
#coding=utf-8
#笨办法学 Python-第四十五题
#关于类,对象,从属关系
print '对象属于某个类,而某个类又属于另一个类,比如小方是泥鳅的成员,而泥鳅又是鱼的成员'
print 'is-a(是啥)---->要用在谈论“两者以类的关系互相关联”的时候,has-a(有啥)---->要用在“两者无共同点,仅是互为参照”的时候'
print '是啥指的是鱼和泥鳅的关系,而有啥指的是泥鳅和鳃的关系'

class Animal(object):
    def __init__(self):
        print 'Animal has life'
class dog(Animal):#继承Animal
    def __init__(self,name):
        self.name=name
    def display(self):
        print self.name

class Cat(Animal):
    def __init__(self,sex):
        self.sex=sex
    def display(self):
        print self.sex

class Person(object):
    def __init__(self,name):
        self.name=name
        self.pet=None
    def display(self):
        print self.name
        print self.pet
class Employee(Person):
    def __init__(self,name,salary):
        super(Employee,self).__init__(name)
        self.salary=salary
    def dispaly(self):
        print self.name
        print self.pet
        print self.salary

dog=dog('二哈')
dog.display()
cat=Cat('male')
cat.display()

tom=Person('tom')
tom.display()
frank=Employee('frank',10000)
frank.pet=dog.name
frank.dispaly()