#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:19:25 2024

@author: vivienneho
"""

class BasicMathOperators:
    
    def __init__(self, firstname, lastname, num1, num2, operator, argument):
        self.firstname = firstname
        self.lastname = lastname
        self.num1 = num1
        self.num2 = num2
        self.operator = operator
        self.argument = argument
        
        
    def greetUser(self):
        print("Greetings "+ self.firstname, " "+ self.lastname)
        
    def addNum(self):
        summ = self.num1 +self.num2
        return summ
    
    def performOperator(self):
        if self.operator=="addition":
            return self.addNum()
        if self.operator=="subtraction":
            return self.num1 - self.num2
        if self.operator=="multiplication":
            return self.num1*self.num2
        if self.operator=="division":
            return self.num1/self.num2
            
    def calculateSquare(self):
        return self.num1**2
    
    def factorial(self):
        fact = 1
        for i in range(1, self.num1+1):
            fact = fact*i
        return fact
        
    def counting(self):
        for i in range(self.num1, self.num2+1):
            print(i)
            
    def calculateHypotenuse(self):
        base = self.calculateSquare()
        perpendicular = self.calculateSquare()
        hyp_squared = base + perpendicular
        hyp = hyp_squared**(1/2)
        return hyp
    
    def areaofRect(self):
        area = self.num1*self.num2
        return area
    
    def powerNum(self):
        return self.num1**self.num2
    
    def argType(self):
        return type(self.argument)
    
 #============================================================================= 
    
def main():
    obj = BasicMathOperators("Vivienne", "Ho", 5, 20, "multiplication", 9)
    function = int(input("""Enter the number that corresponds with what you want to do:
                         1. Add Numbers
                         2. Perform an operation
                         3. Square a number
                         4. Find a factorial
                         5. Count
                         6. Compute hypotenuse
                         7. Find area of rectangle
                         8. Compute power of a number
                         9. Find the type of an argument"""))
                         
    if function == 1:
        print(obj.addNum())
    else:
        if function == 2:
            print(obj.performOperator())
        else:
            if function ==3:
                print(obj.calculateSquare())
            else:
                if function ==4:
                    print(obj.factorial())
                else:
                    if function==5:
                        print(obj.counting())
                    else:
                        if function ==6:
                            print(obj.calculateHypotenuse())
                        else:
                            if function ==7:
                                print(obj.areaofRect())
                            else:
                                if function ==8:
                                    print(obj.powerNum())
                                else:
                                    if function ==9:
                                        print(obj.argType())
                                    else:
                                        print("Invalid selection. Please restart program.")
  #=============================================================================  

main()

        
            
            
            
            
            
            
            
            