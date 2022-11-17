# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 23:17:06 2022

@author: dhpcap
"""

# =============================================================================
'''
Q1.Reverse the following tuple
        aTuple = (10, 20, 30, 40, 50,60)
        Expected output:
        (60,50, 40, 30, 20, 10)
''' 

def addTuple(num):
    aList=[]
    for i in range(1,num+1):
        lst=int(input(f"{i} value of Tuple = "))
        aList.append(lst)
    return aList
def printTuple():
    print(bTuple)
    
def tupRev(bTuple):
    for i in reversed(bTuple):
        print(i)

choice=0
while choice!=4:
    
    choice=int(input("1.Add Element to Tuple\n2.Print the Tuple\n3.Reverse the Tuple\n4.Exit\n"))
    if choice==1:
        num=int(input("What size of tuple u want ? = "))
        bTuple=tuple(addTuple(num))
    
    elif choice==2:
        printTuple()

    elif choice==3:
        tupRev(bTuple)
        
    elif choice==4:
        print("Thank you for visiting..")
    



# =============================================================================

# =============================================================================
'''
Q2. display value 20 from the following tuple
    aTuple = ("Orange", [10, 20, 30], (5, 15, 25))

'''

aTuple=([3,4,5], [10, 20, 30], (5, 15, 25))

#Simple
bTuple=aTuple[1]
print(bTuple)
print(bTuple[1])
num=20

#Menu_Driven
def addTup(num):

    for i in range(1,num+1):
        tup=int(input(f"Enter element for {i} = "))
        a.append(tup)
        b=tuple(a)
        print(b)
    
    
  
def finder(num):
    if num in aTuple:
        i=aTuple.index(num)
        print(f"Value found at index {i}")
    else: 
       for i in range(3):
            a=aTuple[i]
            for j in range(3):
                if a[j] ==num:
                    print(f"{num} found at index={i} subindex={j}")

a=[]
choice=0
while choice!=3:
    choice=int(input("1.Create Tupple\n2.Find elements in Tuple\n3.Exit\n="))
    if choice==1:
        num=int(input("How much elements u need for Tuple = "))
        addTup(num)
    elif choice==2:
       num=int(input("Enter the value to search  = "))
       finder(num)
    elif choice==3:
       print("Thank you for visiting...")
    

# =============================================================================

# =============================================================================
'''
Q. Swap the following two tuples
    tuple1 = (11, 22)
    tuple2 = (99, 88)
    Expected output:
    tuple1 = (99, 88)
    tuple2 = (11, 22)

'''
#Simple

tuple1=(11,22)
tuple2=(99,88)

temp=tuple2
tuple2=tuple1
tuple1=temp
print(f"Tuple 1--> {tuple1}")
print(f"Tuple 2 --> {tuple2}")

#Menu Driven
def tupSwap(tuple1,tuple2):
    temp=tuple2
    tuple2=tuple1
    tuple1=temp
    print(f"Tuple-1 --> {tuple1}")
    print(f"Tuple-2--> {tuple2}")

def tupInsert(num):
    aList=[]
    bList=[]
    for i in range(1,num+1):
        a=int(input(f"Enter tuple1-{i} Element --> "))
        aList.append(a)
        tuple1=tuple(aList)
        

    for i in range(1,num+1):
        b=int(input(f"Enter tuple2-{i} elements --> "))
        bList.append(b)
        tuple2=tuple(bList)
    
    return tuple1,tuple2 # to return 2 values needed to use single return only

choice=0
while choice!=3:
    print("1.Make Tuple\n2.Swap Tuple\n3.Exit\n")
    choice=int(input("Enter u r choice = "))
    if choice==1:
        num=int(input("Enter the size of Tuple = "))
        tuple1,tuple2=tupInsert(num)
        print(f"tuple1 --> {tuple1}")
        print(f"tuple2 ---> {tuple2}")
    elif choice==2:
        tupSwap(tuple1,tuple2)
    else:
        print("Thank You for Visiting.....")




# =============================================================================


# =============================================================================
'''
Q. Copy element 44 and 55 from the following tuple into a new tuple
    tuple1 = (11, 22, 33, 44, 55, 66)
    Expected output:
    tuple2: (44, 55)
'''
#Simple
tuple1=(11,22,33,44,55,66)
a=tuple1[0]
type(a)
tuple1.index(11)
a=list(tuple1)
tuple2=tuple(a[3:5])
print(tuple2)

#Menu Driven

aList=[]
num=int(input("Enter size of your Tuple = "))
for i in range(num):
    a=int(input("Enter the element u want to add = "))
    aList.append(a)
    tuple1=tuple(aList)
    print(tuple1)

#tuple2=[] ---> if we want list not to reset
ans="y"
while ans =="y":
    tuple2=[]    # List will be reset
    num=int(input("How many values u want to copy = "))
    for i in range(num):
        num1=int(input("Enter number to copy = "))
        if num1 in tuple1:
            a=tuple1.index(num1)
            tuple2.append(tuple1[a])
            print("value --> ",tuple2)
        else:
            print("Number not found") 

    ans=input("Do you want to continue = (y/n) -->")
#ans=input("Do you want to continue = (y/n) --> ) It will create infinite loop
 



# =============================================================================

# =============================================================================
'''
Q6. Modify the first item (22) of a list inside a following tuple to 200
    tuple1 = (11, [22, 33], 44, 55)
    Expected output:
        tuple1: (11, [200, 33], 44, 55)
        
'''
tuple1 = [11 , [200, 33] , 44 , 55]

lst=[]
num=int(input("Enter the old value = "))
new=int(input("Enter the new value = "))
if num in tuple1:
    a=tuple1.index(num)
    tuple1[a]=new
    print(tuple1)
else: 
   for i in range(3):
        a=tuple1[i]
        for j in range(3):
            if a[j] ==num:
                print(f"{num} found at index={i} subindex={j}")


        
# =============================================================================
