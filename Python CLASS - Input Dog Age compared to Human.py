# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 11:19:40 2021

@author: Anthony
"""

class Doggy:
    years = 0
    def dog_real_age(its):
        if age <= 0:
            return "Not Funny"
        if age == 1:
            return "15"
        if age == 2:
            return "24"
        else:
            return (((its.years - 2) * 4) + 24)
'''
First year of dog age = 15 human age, second year = 24yo human age and the rest * 4
'''
dog = Doggy()
age = int(input("Please input your dog's age: "))
dog.years = age
print(dog.dog_real_age())