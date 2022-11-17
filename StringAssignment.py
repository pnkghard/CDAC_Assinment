=# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 21:17:03 2022

@author: dhpcap
"""

# =============================================================================
'''
Given a string of odd length greater than 7, return a new string made of the middle three
characters of a given String
Given:
str1 = "RakeshzipPetabb"
Output
 zip

'''

str1 = "RakeshzipPetabb"
print(str1[6:9])

str2 = "JazzbonAyxx"
print(str2[4:7])

ans="y"
while ans=="y":
    s=input("Enter the string greater than 7")
    l=len(s)
    d=l//2

    print(s[d-1:d+2]) # +2
    ans=input("continue (y/n)")
# =============================================================================


# =============================================================================
'''
Q2. Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
        Given:
        s1 = "Ault"
        s2 = "Kelly"
        Expected Output:
        AuKellylt
''' 

s1="Ault"
st=s1.split("Au") 
print(st)
st2=s1.split("lt")

s1="Ault"
s2 = "Kelly"

for i in s1:
    print(i,end="")
    if i=="u":
        print(s2,end="")
    

# =============================================================================

# =============================================================================
'''
Q3. two strings, s1, and s2 return a new string made of the first, middle, and last characters each
    input string
        Given:
            s1 = "America"
            s2 = "Japan"
            Expected Output:
                AJrpan

'''
def mix(x,y):
    len1=len(x)
    len2=len(y)
    first=x[:1]+y[:1]
    middle=x[len1//2:(len1//2)+1]+ y[len2//2:(len2//2)+1]
    last=x[-1]+y[-1]
    combi=first+middle+last
    print(combi)
    
s1=input("Enter string first = ")
s2=input("Enter string two = ")
mix(s1,s2)



# =============================================================================

# =============================================================================

'''
Q4. Given an input string with the combination of the lower and upper case arrange characters
    in such a way that all lowercase letters should come first.
    solution:
        str1 = "PytHONStudy"
''' 
str1 = "PytHONStudy"
lower = []
upper = []
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sorted_string = ''.join(lower + upper)
print("arranging characters giving precedence to lowercase letters:")
print(sorted_string)

       
        
    
# =============================================================================

# =============================================================================
'''
Q5. create a third-string made of the first char of s1 then the last char of s2, Next, the second
    char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the
    result.
    Given:
        s1 = "Abc"
        s2 = "Xyz"
        Expected Output: AzbycX
        
'''
def mix(x,y):
    len1=len(x)
    len2=len(y)
    
    
    

    


 
# =============================================================================
