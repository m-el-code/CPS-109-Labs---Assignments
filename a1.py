# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 18:56:22 2022

"""

#Assignment 1
#Manar Elbeshbishy
#501089420

#Problem: Create a program to calculate the grade needed on the final to get 'x' grade as a final mark, and determine if it is a passing grade in the course.

#opens the output.txt file and appends the desired outputs to it
f = open("output.txt", "w") 

#defining the overall function for the calculator
def finalGradeCalculator():
    
  #asks for user input of grade, if the grade is unknown, asks the user to enter a preset input; assigns input to variable
  oGrade = input("\nEnter your overall grade in the course, if overall grade is unknown, enter 'U': ")
  
  #if the user inputs grade as unknown, runs through the if statement
  if oGrade == 'U' or oGrade == 'u':
    
    #asks for user input of the grades received so far, assigns input to variable
    grades = input("Enter individual grades recieved, sperated by a space: ").split(" ")
    
    #function used to find th average of grades inputted from the user
    def gradesAverage(grades):
      
      a = 0 #sets an arbitrary variable to sum up the grades
      
      #for loop runs through the length of the string, which is the user input 
      for x in range(len(grades)):
      
        n = float(grades[x]) # converts every grade into a float number, and assigns to variable
        a = (a + n) #adds every grade together as the for loop runs through the iteration; 
                    #done by reassigning variable a to the summed up number and adding to that every iteration
      a = a / (len(grades)) #after running through the for loop, takes the summed up grades and divides by the number of grades; finding average
      return a #function returns the value of the average
      
    avgGrade = gradesAverage(grades) #sets the return value of the function into variable 
    
    print(f"\nGrade in course so far is: {avgGrade}%", file = f) #prints output of the average grade in the course to the text file
    
  else: #else statement runs if the user entered their average grade
    avgGrade = oGrade  #assigns the user inputed grade to variable 
    
    
    print(f"\nCurrent grade in the course is {avgGrade}%", file = f) #prints the current grade that the user hasin the course to the text file
    
  #asks user input for their desired grade in the course; assigns to variable
  fGrade = float(input("\nEnter desired grade in the course: ")) 
  
  #asks user input for the weight of the final; assigns to variable
  weight = float(input("Enter the weight of the final: "))
  
  #converts weight into a decimal number for use within code
  weight = (weight / 100)
  
  #formula to find the lowest mark needed to pass the course with given average
  lMark = (50 - ((1 - weight) * float(avgGrade))) / weight
  
  #formula to calculate the grade the user will pass with at the current mark
  pGrade = ((1-weight)*float(avgGrade)) + (weight*0)
  
  #function to determine if the mark user has in course is already a passing grade
  def lowestGrade(lMark):
      
    if lMark <= 0: #checks to see if the lowest mark needed is 0 or less, then sets value to true (passing)
      return True
  
    else: #if the lowest mark calculated is greater than 0, sets value to false (failing)
      return False
      
  #function to calculate the final grade needed on the final
  def finalGrade(avgGrade):
    
    #calculation uses the final grade wanted, the weight and given average to find the final mark needed
    fMark = (fGrade - ((1 - weight) * float(avgGrade))) / weight
    
    #returns the value of the final mark calculated within the function
    return fMark
  
  #checks to see if the user is already passing the course with the current mark in the course
  if lowestGrade(lMark):
    
    #if passing, prints statement stating:
    print(f"\nYou do not need to take the final to pass the course, you will pass with a {round(pGrade, 2)}%", file = f)
    
  #if user is not passing the course with the current mark in the course, runs through else: 
  else:
    
    #prints statement stating a fail
    print (f"\nLowest grade needed to pass the course is: {round(lMark, 2)}%", file = f)
  
  #prints the output of the mark that the user needs to get on the final to get the desired grade in the course 
  print(f"\nThe final grade needed is: {round(finalGrade(avgGrade), 2)}%", file = f)  
  
finalGradeCalculator() #calls function so it runs once before executing next user input

#infnite while loop to run the program as many times as the user wishes, will run until broken in the 'elif' statement
while True:
    
  #asks for user input if they would like to run the calculator again, assigns to variable
  runAgain = input("\nWould you like to calculate a different mark? Enter 'Yes' or 'No': ")

  #converts the user input into all lower case letter
  runAgain = runAgain.lower()

  #if the user indicated yes to run the calculator again, the calculator function is called
  if runAgain == 'yes':
    finalGradeCalculator()
  
  #if the user indicated no to stop the program...
  elif runAgain == 'no':
      
    #prints a final statement concluding use of calculator if they indicated they did not want to use the calculator again
    print ("\nThank you for using the Grade Calculator! Have a nice day!", file = f)  
    
    f.close() #closes the file once function is done running
    
    break #breaks the while loop and stops running the program
    
  #else statement if the use does not provide a valid input
  else:
    
    #prints a statement stating an invalid input, will then run the loop again until a valid input is entered
    print ("\nThat is not a valid input. Please enter a valid input.")
    

