#/usr/bin/puthon
#encoding=utf8
#笨办法学 Python-第四十六题
#了解项目的架构
print'''
项目架构为:
.
└── skeleton
    ├── bin
    │   └── setup.py
    ├── docs
    ├── NAME
    │   ├── __init__.py
    │   └── __init__.pyc
    └── tests
        ├── __init__.py
        ├── __init__.pyc
        ├── NAME_tests.py
        └── NAME_tests.pyc

NAME_tests.py
from nose.tools import *
import NAME
def setup():
    print "SETUP!"
def teardown():
    print "TEAR DOWN!"
def test_basic():
    print "I RAN!"

'''