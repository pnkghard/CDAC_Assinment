# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 21:47:19 2022

@author: dhpcap
"""

keys = ['Ten','Twenty','Thirty']
values = [10,20,30]

print(dict(zip(keys,values)))

d={}
for i in range(3):
    d[keys[i]]=values[i]
print(d)    
    
for key,value in zip(keys,values):
    print(f"{key}:{value}")


dict1 = {'Ten':10,'Twenty':20,'Thirty':30}
dict2 = {'Thirty':30,'Fourty':40,'Fifty':50}

dict3 = {**dict1,**dict2}
print(dict3)    

sampleDict = {
"class":{
"student":{
"name":"Mike",
"marks":{
"physics":70,
"history":80
}
}
}
}

print(sampleDict['class']['student']['marks']['history'])


#4 Delete set of keys from a dictionary

sampleDict = {
    "name" : "Kelly",
     "age" : 25,
     "salary" : 8000,
     "city" : "New york"
    
    }

keys = ["name", "salary"]

for k in keys:
    sampleDict.pop(k)
    print(sampleDict)


sampleDict = {
    'a' : 100,
    'b' : 200,
    'c' : 300,
    'd' : 200
    }
if 200 in sampleDict.values():
    print("200 present im ")




sampleDict = {
    'Physics': 82 ,
    'Math' : 65 ,
    'history' : 75 
    }
    
print(max(sampleDict))
    



sampleDict = {
    'emp1' : {'name':'Jhon','salary':7500},
    'emp2' : {'name':'Emma','salary': 8000},
    'emp3' : {'name': 'Brad','salary' : 8500}

}   

emp_name = input("enter the name : ")


for key,value in sampleDict.items():
    for key1,value1 in  value.items():
        if value1 == emp_name :
            print("name found")
            new_salary = int(input("enter the salary"))
            
        elif new_salary > sampleDict['emp1']['salary']  :
              value['salary'] = new_salary
              print("Salary Modified")
              continue
        elif  new_salary < sampleDict['emp1']['salary'] :
            print("wrong salary")
            break
        else:
            print("name not found")
            break
            
        
        











