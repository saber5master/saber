# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 15:26:33 2017

@author: ice-fire
"""
#==============================================================================
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def __setattr__(self, name, value):
#         super().__setattr__(name, value)
#         if name == 'square':
#             self.width = value
#             self.height = value
#         else:
#             name = value
# #        super().__setattr__(name, value)
#         
#     def getArea(self):
#         area = self.width * self.height
#         return area
#         
# rec = Rectangle(3, 4)
# print(rec.getArea())
# 
# rec.square = 10
# print(rec.getArea())
#==============================================================================
 

class MyProperty:
    def __init__(self, fget = None, fset = None, fdel = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner):
        return self.fdel(instance)
    def __set__(self, instance, value):
        self.fset(instance, value)
    def __delete__(self, instance):
        self.fdel(instance)
        
class C:
    def __init__(self):
        self._x = None
    def getX(self):
        return self._x
    def setX(self, value):
        self._x = value
    def delX(self):
        del self._x

x = MyProperty(getX, setX, delX)



























