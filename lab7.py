# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:23:59 2022

"""

#Lab 7
#Manar Elbeshbishy

import random

def question_1 ():
    run = [random.randrange(1,7) for x in range(20)]
    inRun = False

    for x in range(len(run)):
        if inRun:
            if run[x] != run[x-1]:
                print (")", end  = '')
                inRun = False
        if x != len(run)-1:
            if run[x]==run[x+1] and not inRun:
                print ("(", end = '')
                inRun = True
        print (run[x], end = '')
    if inRun:
        print(")", end = '')


def question_2 ():
    run = [random.randrange(1,7) for x in range(20)] 
    count = 0
    tempLongest = 0
    for x in range(len(run)-1):
        if run[x] == run[x+1]:
            count += 1
        else:
            count = 0
        if count > tempLongest:
            tempLongest = count
            start = x - tempLongest + 1
            end = x + 1

    for x in range(len(run)):
        if x == start:
            print('(', end = '')
        print(int(run[x]), end = '')
        if x == end:
            print(')', end = '')
        


def longestFalse(L):
    enumBoolList = list(enumerate(L))
    count = 0
    tempLongest = 0
    for index, value in enumBoolList:
        if value == False:
            count += 1
        else:
            count = 0
        if count > tempLongest:
            tempLongest = count
            start = index - tempLongest + 1
            end = index 

    return((start, end)) 




def occupy(n):
    run = [' _ ' for x in range(n)]
    newRun = []
    for x in run: #prints first line
        print(x, end = ' ')
    print ("\n")
    for x in range(len(run)): #creates false list
        if run[x] == ' _ ':
            newRun.append(False)
            
    for x in range(n): #runs num_iterations (input) 
        nest = longestFalse(newRun) #index of the largest grouping
        replaceNest = (nest[1]+nest[0]+1)//2 #midpooint of nest
        run[replaceNest] = ' X ' #replaces OG list
        newRun[replaceNest] = ' X ' #replaces false list
        for x in run: #prints array
            print(x, end = ' ')
        print ("\n")
              

def isPal(L):
    reverseL = L.copy()
    reverseL.reverse()
    if L == reverseL:
        return True
    else:
        return False


print("Question 1: ")            
question_1()

print("\n\nQuestion 2:")
question_2()

print("\n\nQuestion 3: ")
print(longestFalse([False, False, True, False, False, False, False, True, True, False, False]))

print("\n\nQuestion 4: ")
occupy(10)

print("\nQuestion 5: ")
print(isPal([5,2,9,9,2,5]))