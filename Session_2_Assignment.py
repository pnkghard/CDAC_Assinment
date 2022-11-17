"""
    Write a program that asks the user how many days are in a particular month, and
    what day of the week the month begins on (0 for Monday, 1 for Tuesday, etc), and
    then prints a calendar for that month. For example, here is the output for a 30-day
    month that begins on day 4 (Thursday):
        
        S   M  T  W  T  F  S
                     1  2  3
        4   5  6  7  8  9 10
        11 12 13 14 15 16 17
        18 19 20 21 22 23 24
        25 26 27 28 29 30
"""

days = int(input("Days in month : "))
day = int(input(""" 
          1 for Monday
          2 for Tuesday
          3 for Wenusday
          4 for Thursday
          5 for Friday
          6 for Saturday
          7 for Sunday 
  Enter the value : """))
import numpy as np
array = np.arange(1, days+1)

       
"""    
    procedure histogram() that takes a list of integers and prints a histogram
    to the screen. For example, histogram([4, 9, 7]) should print the following:
        
         ****
        *********
         *******
"""
"""
    Write a version of a palindrome recognizer that also accepts phrase palindromes
    such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no
    pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my
    metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the
    exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing
    are usually ignored.
"""
"""
    A pangram is a sentence that contains all the letters of the English alphabet at
    least once, for example: The quick brown fox jumps over the lazy dog. Your task
    here is to write a function to check a sentence to see if it is a pangram or not.
"""