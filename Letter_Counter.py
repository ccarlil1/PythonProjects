# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 21:12:55 2019

@author: Casey
"""

import string

def counter(phrase):
    count_letters = {}
    all_letter_count = {}
    alphabet = string.ascii_letters
    
    for i in alphabet:
        count = 0
        for j in sentence:
            if i == j:
                count += 1
        all_letter_count[i] = count
    
    for k in all_letter_count:
        if all_letter_count[k] > 0:
            count_letters[k] = all_letter_count[k]
            
    return count_letters

print("Type a phrase to count letters. Then press enter.")

while True:
            
    sentence = input()
    
    if sentence == "q" or sentence == "Q":
        break;
        
    print(counter(sentence))        
    
    print("Enter a new phrase or type 'Q' to quit")
    
            
        