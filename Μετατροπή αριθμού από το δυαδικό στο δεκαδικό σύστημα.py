# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:37:49 2021

@author: nikomahos
"""

#Μετατροπή αριθμού από το δεκαδικό στο δυαδικό σύστημα.
num1=int(input("Please enter a number: "))
quotient=int(num1/2)
remainder=num1%2
binary=[]
binary.append(remainder)
while remainder!=1 or quotient!=0 : 
    quotient1=int(quotient/2)
    remainder=quotient%2   
    quotient=quotient1
    binary.append(remainder)
binary.reverse()
print(binary)