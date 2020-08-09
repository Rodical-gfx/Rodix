# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 16:13:33 2020

@author: SUCCESS-PC
"""
print('ALPHABET PRINTS\n'   '****PROGRAM****')
            
print('\n ')
for num in range(5):
    if num ==0:
        for c in range(6):
            if c ==0 :
                print(' ', end='')
            elif c==5:
                print(' ')
            else:
                print('#', end='')
                ########
        
    if num !=0 and num !=3:
        for c in range(6):
            if c ==0 :
                print('#', end='')
            elif c==5:
                print('#')
            else:
                print(' ', end='')
    if num==3:
        for c in range(6):
            print('#', end='')
            if c==5:
                print('')
            
print('\n ')          
for num in range(5):
    if num ==0:
        for c in range(6):
            if c ==0 :
                print('#', end='')
            elif c==5:
                print(' ')
            else:
                print('#', end='')
                ########
        
    if num !=0 and num !=2 and num !=4:
        for c in range(6):
            if c ==0 :
                print('#', end='')
            elif c==5:
                print('#')
            else:
                print(' ', end='')
    if num==2:
        for c in range(5):
            print('#', end='')
            if c==4:
                print('')
    if num==4:
        for c in range(5):
            print('#', end='')
            if c==4:
                print('')
                
print('\n ')          
for num in range(5):
    if num ==0:
        for c in range(6):
            if c ==0 :
                print('#', end='')
            elif c==5:
                print(' ')
            else:
                print('#', end='')
                ########
        
    if num !=0 and num !=2 and num !=4:
        for c in range(6):
            if c ==0 :
                print('#')#, end='')
            #elif c==5:
             #   print('#')
            #else:
             #   print(' ', end='')
    if num==2:
        for c in range(5):
            #print('#', end='')
            if c==1:
                print('#')
    if num==4:
        for c in range(5):
            print('#', end='')
            if c==4:
                print('')