# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:27:40 2022

@author: dhpcap
"""

def factorial(num):
    '''this function returns factorial of a number'''
    f=1
    for i in range(1,num+1): #1,2,3,4,5
        f=f*i
    return f

   # num=int(input("enter number"))
   # ans=factorial(num)
   # print(ans)
       
    
 # addition function    
def addition(a,b):
     a=a+10
     b=b+15 
     return a+b
#ans=addition(3,3)
#print(ans)
 
#ans=addition(b=10,a=30)
#print(ans)   

# print table1

def printtable(n):
    for i in range(1,11):
        
        print(f"{n}*{i}={n*i}")
        
# for choice 
choice = 0
while choice != 4 :
    choice=int(input("1. factorial \n 2. addition \n 3. printtable \n 4. exit \n choice:"))
# perform the task
    if choice == 1:
       num = int(input("enter number"))
       ans=factorial(num) 
       print(ans)
    elif choice==2:
         a = int(input("enter number"))    
         b = int(input("enter number")) 
         ans=addition(a,b)
         print(f"addition : {ans}")
    elif choice==3:
        n=int(input("enter number"))
        printtable(n)
    elif choice==4:
        print(" thank you for visting ...")    
        