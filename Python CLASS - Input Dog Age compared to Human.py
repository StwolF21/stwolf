# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 11:19:40 2021

@author: Anthony
"""

class Doggy:
    years = 0
    def dog_real_age(its):
        return its.years * 15 # General consensus: A dog's year = 15 years of human life

dog = Doggy()
age = int(input("Please input your dog's age: "))
dog.years = age
print(dog.dog_real_age())
