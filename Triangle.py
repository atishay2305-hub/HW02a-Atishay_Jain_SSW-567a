# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
@author: Atishay Jain
"""

def classifyTriangle(a,b,c):

    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    try:
        if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
            return 'InvalidInput'; #error will occur as ";" is appearing unnecessarily

    except:
        print('The value is incorrect')
    
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'  
    # now we know that we have a valid triangle 
    if a == b and b == c and a == c: 
        return 'Equilateral' #checking whether the triangle is equilateral or not
    elif ((a ** 2) + (b ** 2)) == (c ** 2) or ((b ** 2) + (c ** 2)) == (a ** 2) or ((a ** 2) + (c ** 2)) == (b ** 2):
        return 'Right'      #checking whether the triangle is Right Triangle or not
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene' #checking whether the triangle is Scalene or not
    else:
        return 'Isoceles' #checking whether the triangle is Isoceles or not

# if __name__ == '__main__':
    