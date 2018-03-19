# -*- coding: utf-8 -*-
'''
Created on 2017年3月28日
@author: guanglin
decorator
'''
def inner():
    print('hey,inner.')
def out(func):
    print('loading '+func.__name__)
    func()

out(inner)

class Stu(object):
    def __init__(self,name,score):
        self.name=name
        self.score1=score
    
    @property
    def score(self):
        return self.score1
    
    @score.setter
    def score(self,value):
        if value<0 or value > 100:
            print("Value Error.")
        else:
            self.score1=value
            
    def __call__(self):
        print('cao')
    
#             
s1=Stu('Lilei',100)
print(s1.score)
# print s1.score
s1()