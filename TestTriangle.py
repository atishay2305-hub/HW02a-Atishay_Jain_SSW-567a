# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: Atishay Jain
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testifTriangle(self):
        self.assertEqual(classifyTriangle(10,4,3), 'NotATriangle', '10,4,3 is not a triangle')
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(8,8,10), 'Isoceles', '8,8,10 should be Isosceles')
    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(3,3,4), 'Isoceles', '3,3,4 should be Isosceles')
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(2,3, 4), 'Scalene', '2,3,4 should be Scalene')
    def  testStringTriangle(self):
        self.assertEqual(classifyTriangle('a','b','c'), 'InvalidInput', 'a,b,c should not be a triangle')
    def testTriangleSides(self):
        self.assertEqual(classifyTriangle(10,-10,-20), 'InvalidInput', '10,-10,-20 should not be a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()




