# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:14:59 2022

@author: dhpcap
"""

#Q1. Accept 10 integers from user and print their average value on the screen

sum1=0
for i in range(10):
    num=int(input(f"Enter the number {i} = "))
    sum1=sum1+num

avg=sum1/10

print(f"Average is = {avg}")

#----------------------------------------------------------------------------------------------

#2. Print the following patterns using loop :

    
#1)
for i in range(1,5):
    print("*"*i)
    
#2)
for i in range(1,5,2):
    if i==1:
        print("",end="  ") # 2 spaces
    if i==3:
        print("",end=" ")   # 1 spaces
    print("*"*i)
for i in range(5,0,-2):
    if i==3:
        print("",end=" ")   # 2 spaces
    if i==1:
        print("",end="  ")   # 1space
    print("*"*i)
    
#3) 

#4)
for i in range(1,7):
    for j in range(1,i):
        print(j,end="")
    print("")    
#-----------------------------------------------------------------------------------------

#Q4.Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.
       
num1=int(input("Enter first number = "))
num2=int(input("Enter the second number = "))

for i in range(10,1,-1):
    if num2%i==0 and num1%i==0:
        print(f"Greatest Common Divisor = {i}")
        break
print("End of program....")

# Finding the HCF

temp=1
while num2 > 0:
    temp = num2;
    num2 = num1% num2; 
    num1 = temp;
print(f"HCF = {num1}")
#--------------------------------------------------------------------------------------------

#Q5. Given a number count the total number of digits in a number and also find sum of digits of the number
    
num1=int(input("Enter the number = "))
count=0
while num1>0:
    
    rem=num1%10
    sum=sum+rem*10
    num1=num1//10
    count=count+1
print(f"total number count = {count}")
print(f"total number count = {sum}")
    
#---------------------------------------------------------------------------------------------------

#Q6. To display the cube of the number upto given an integer. If the given integer is 5, then display cube of 1 to 4.

num1=int(input("Enter the number = "))
count=0

while num1>0:
    count=count+1
    num1=num1//10
print(f"Total count = {count}")

for i in range(1,count+1):
    print(f"Cube of the {i} = {i*i*i}")
    
#-------------------------------------------------------------------------------------
    
#Q7. Accept 20 numbers from user and display sum of only even numbers.

sum=0
for i in range(1,5):
    num=int(input(f"Enter the values for {i} = "))
    if num%2==0:
        sum=sum+num
print(f"Sum of even numbers = {sum}")

#-----------------------------------------------------------------------------------------


#Q8.Ask user number of terms to be generated of a series. generate numbers for the following series and find its addition [9 + 99 + 999 + 9999+……..]

step = int(input("Enter the number of Steps = "))
sum1=0
a=0
for i in range(1,step+1):
    sum1=sum1+9
    sum1=(sum1*10)
    a=a+sum1
print(f"Sum for {step} steps of 9  = {a}")

#----------------------------------------------------------------------------------------


#Q9. Write a program in python to display the sum of the series [ 1+x+x^2/2!+x^3/3!+....]
    #x= 3 and input terms =5 and ans=== 16.375000
    
for num in range(1,6):
    for i in range(1,num):
        num=num*i
print(num)
    
intList = [1,2,3,4,5]
for x in range(1,6):
    series=map(lambda x: x*intList )

list(series)
