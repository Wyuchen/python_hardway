#!/usr/bin/python
#encoding=utf8
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config={
    'description':'skeleton',
    'author':'wz',
    'url':'url to get it at.',
    'download_url':'where to download it',
    'author_email':'123456@qq.com',
    'version':'0.1',
    'install_requires':['nose'],
    'packages':['NAME'],
    'scripts':[],
    'name':'projectname'
}

setup(**config)

