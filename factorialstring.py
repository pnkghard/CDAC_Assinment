# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:50:55 2022

@author: dhpcap
"""

def factorial(n=5):
    f=1
    for i in range(1,n+1):
        f= f*i
        return f 
    
x = int(input("enter x"))
term = int(input("enter terms"))
s = 1
print( f"{s}", end = " ")
    
for i in range(1,term):
    a = x ** i 
    f = factorial(i)
    print(f"+{x}^{i}/{i}!", end=" ")
    s = s + (a/f)
    print(f"={s}")
    

s ="iuieuriou"
print(id(s))
s="nbxcvxb"
print(id(s))
s = 10 
h = 10
print(id(s),id(h))
print(s is h)
s = 23
print(s is h)

lst = [12,13,14]
for index,num in enumerate(lst):
    print(f"{index}------>{num}")
    

lst = [40,80,30,50,60,80]
names = ["pune","mumbai","delhi","jalgoan"]

for num,nm in zip(lst,names):
    print(f"{num}-----.{nm}")
    
for num in sorted(lst):
    print(num)
    print(lst)
    
lst = [40,80,30,50,60,80]    
for num in reversed(lst):
    print(num)
    print(lst)   
    
lst = [12,13,14,5,3,4,27,5,6]
lst1 = []
for num in lst:
    lst1.append(num*num)
lst1 = [num*num for num in lst]
 
lst1 = list(map(lambda x:x*x,lst))
print(lst1)   

lst1 = []
for num in lst:
    if num > 10:
       lst1.append(num)
       print(lst1)
        
lst1 = [num for num in lst if num > 10 and num % 3 == 0]
print(lst1)    
    
lst2 = list(filter(lambda x:x > 10 and x%3 == 0 , lst))
print(lst2)

words = ["hello","welcome","aaaa","try","test","te"]
lst3 = list(filter(lambda x:len(x)>=4,words))
print(lst3)

lst4 = list(filter(lambda x:x.startswith("we"),words))

from functools import reduce
ans = reduce(lambda x,y:x+y,lst)
print("addition :" , ans)

lst = ["python","perl","Java","c++"]
s = reduce(lambda x,y:x+y[0:2],lst,"")
print(s)    
    
    
a = 12 ,13 ,"Rajas"
b = (10,20,30)

x = b[0]
y = b[1]
z = b[2]

x,y,z = b 

a = 12,12,10,12,3,4,12
print(a.count(12))
if 3 in a :
    print(a.index(3))
    
def f1(x,y):
    x = x+10
    y = y+20    
    return x,y

x,y = f1(23,24)

a,b = f1(23,45)
print(x,y)
print(a,b)

a = 12
b = 100 
a,b = b,a
print(a,b)

a = 12
a = 12
print(type(a))    


def f2(x,y,*t):
    print(x,y)
    print(t)
    
def addition(x,y,*t1):
    ans = x + y 
    for n in t1:
        ans = ans + n 
        return ans
 
f2(1,2)
f2(1,2,3,4,5,6,7,8,9)    
d = addition(1,2)
print(d)  

d = addition(10,2,3,4,5,6,7,8)
print(d)  

















































    
    
    