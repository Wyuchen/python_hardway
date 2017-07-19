#!/usr/bin/python
#coding=utf-8
# 笨办法学 Python-第二十四题
#针对前面的知识的复习和总结
def break_words(stuff):
    words=stuff.split()
    return words
def sort_words(words):
    return sorted(words)
def print_frist_word(words):
    word=words.pop(0)
    print word
def print_last_word(words):
    word=words.pop(-1)
    print word
def sort_sentence(sentence):
    words=break_words(sentence)
    return sort_words(words)
def print_frist_and_last(sentence):
    words=break_words(sentence)
    print words
    print_frist_word(words)
    print_last_word(words)
def print_frist_and_last_sorted(sentence):
    words=sort_sentence(sentence)
    print words
    print_frist_word(words)
    print_last_word(words)

words=break_words("All good things come to those who wait")
print '打印出分隔的单词'
print words
print '返回排序后的结果'
print sort_words(words)
print '打印未排序的首单词'
print_frist_word(words)
print '打印未排序的尾单词'
print_last_word(words)

sentences=sort_sentence('All good things come to those who wait')
print '打印出分隔的单词'
print sentences
print '打印未排序的首尾单词'
print_frist_and_last('All good things come to those who wait')
print '打印排序的首尾单词'
print_frist_and_last_sorted('All good things come to those who wait')