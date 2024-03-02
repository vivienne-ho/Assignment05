#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:19:25 2024

@author: vivienneho
"""


#This creates a class filled with math operator functions
class BasicMathOperators: 
    
   #This initializes the attributes of the object
    def __init__(self, firstname, lastname, num1, num2, operator, argument):
        self.firstname = firstname
        self.lastname = lastname
        self.num1 = num1
        self.num2 = num2
        self.operator = operator
        self.argument = argument
        
    #This greets the user
    def greetUser(self):
        print("Greetings "+ self.firstname, " "+ self.lastname)
        
    #This adds two numbers
    def addNum(self):
        summ = self.num1 +self.num2
        return summ
    
    #This performs a certain operator based on object attributes
    def performOperator(self):
        if self.operator=="addition":
            return self.addNum()
        if self.operator=="subtraction":
            return self.num1 - self.num2
        if self.operator=="multiplication":
            return self.num1*self.num2
        if self.operator=="division":
            return self.num1/self.num2
            
    #This calculates the square of an object
    def calculateSquare(self):
        return self.num1**2
    
    #This finds the factorial of a number
    def factorial(self):
        fact = 1
        for i in range(1, self.num1+1):
            fact = fact*i
        return fact
        
    #This will count starting at a specified number and going to another
    def counting(self):
        for i in range(self.num1, self.num2+1):
            print(i)
            
    #This will calculate the hypotenuse of a right triangle
    def calculateHypotenuse(self):
        base = self.calculateSquare()
        perpendicular = self.calculateSquare()
        hyp_squared = base + perpendicular
        hyp = hyp_squared**(1/2)
        return hyp
    
    #This calculates the area of a rectangle
    def areaofRect(self):
        area = self.num1*self.num2
        return area
    
    #This will calculate the power of a number to another number
    def powerNum(self):
        return self.num1**self.num2
    
    #This returns what data type a variable is
    def argType(self):
        return type(self.argument)
    
 #============================================================================= 
    
def main():
    
    obj = BasicMathOperators("Vivienne", "Ho", 5, 20, "multiplication", 9)
    obj.greetUser()
    
    #This allows the user to choose what they want to do
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
                                        #If the user enters something other then numbers 1-9,
                                        # it will make the user start again.
                                        print("Invalid selection. Please restart program.")
  #=============================================================================  

main()

        
            
            
            
            
            
            
            
            