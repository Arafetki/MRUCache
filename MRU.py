# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:00:06 2022

@author: arafe
"""
from collections import OrderedDict
class MRUCache:
    def __init__(self,c):
        self.cache=OrderedDict()
        self.Capacity=c
    def get(self,key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key,last=True)
            return self.cache[key]
    def put(self,key,value):
        if key not in self.cache:
            if len(self.cache)==self.Capacity:
                self.cache.popitem(last=True)
            self.cache[key]=value
            self.cache.move_to_end(key,last=True)
        else:
            self.cache[key]=value
            self.cache.move_to_end(key,last=True)


