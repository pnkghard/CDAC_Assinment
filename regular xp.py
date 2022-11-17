# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 10:45:21 2022

@author: dhpcap
"""
import re
s="something is there somewhere"
m=re.search("s.*e",s,re.I)
if m!=None:
    print("found")
    print(m.group())
    print(m.span())
else:
    print(" pattern not found")
    
    
    
s="something is there somewhere"
m=re.search("s.*?e",s,re.I)
if m != None:
    print("found")
    print(m.group()) # will give the matching string of given string 
    print(m.span()) # give position
else:
    print(" pattern not found")    
    
import re
s="something is there somewhere"
m=re.search("s(.*)e",s,re.I)
if m!=None:
    print("found")
    print(m.group())
    print(m.span())
    print(m.group(1))
    print(m.span(1))
else:
    print(" pattern not found")    
    
    
    
data=" this is home "
m=re.search("\w+\s\w+\s\w+", data)  
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")   
    
    
# know  
data=" this is home, sweet home "
m=re.search("(\w+)\s(\w+)\s\w+", data)  
if m!=None:
    print(m.group())
    print(m.group(1))
    print(m.group(2))

    print(m.span())
    print(m.span(1))
    print(m.span(2))    
else:
    print("not found")    
        
#    
data=" this is home, sweet home "
m=re.search("^(\w+)\s(\w+)\s\w+$", data)  
if m!=None:
    print(m.group())
    print(m.group(1))
    print(m.group(2))

    print(m.span())
    print(m.span(1))
    print(m.span(2))    
else:
    print("not found") 
    
#
data=" this is home, sweet home "
m=re.search("s.*t", data)  
if m!=None:
    print(" found")
       
else:
    print("not found")    
       

# match 
data=" this is home, sweet home "
m=re.match("s.*t", data)  
if m!=None:
    print(" found")
       
else:
    print("not found")    
       

# findall , only tell strings 

s="something is there somewhere"
lst=re.findall("s.*?e",s,re.I)
if lst!=None:
    print("found")
    print(lst)

else:
    print(" pattern not found")    
    

# finditer, tell strings with position 
s="something is there somewhere"
lst=re.finditer("s.*?e",s,re.I)
if lst!=None:
    print("found")
    for m in lst:
        print(m.group())
        print(m.span())

else:
    print(" pattern not found")    
    

# sub 

sm="something is there somewhere"
lst=re.sub("s.*?e","any",sm,re.I)
if lst!=None:
    print("found")
    print(" original string", sm)
    print(lst)
else:
    print(" pattern not found")    
    

#
sm="something is there somewhere"
lst=re.sub("s.*?e","any",sm,flag=re.I)
if lst!=None:
    print("found")
    print(" original string", sm)
    print(lst)
else:
    print(" pattern not found")    
    

# ***********************
myreg=re.compile("s.*?e",re.I)
sm="something is there somewhere"

m=myreg.search(sm)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print(" not found ")    












    
       