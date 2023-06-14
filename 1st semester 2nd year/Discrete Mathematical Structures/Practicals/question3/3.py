'''
Q3)Write a Program that generates all the permutations of a given set of digits, with or without repetition.
'''
from itertools import permutations      #importing itertools module
def generatePermutations(n,with_repetition=False):       #function with with_repetition=False
   if with_repetition:
      perm=permutations(n,len(n))
   else:
        perm=permutations(n)
   for i in list(perm):          #printing the permutations in list form sequentively
       print (i)
    
def main():    #main Program 
    print("Program to generate all the permutations of a given set of digits with or without permutations.")
    digits=eval(input("enter the digits to be added in the list whose permutation you want to find:"))
    
    permutationsWithoutRepetition=generatePermutations(digits)      #Permutations without repetition
    permutationsWithRepetition=generatePermutations(digits,with_repetition=True)  #Permutations with repetition
    
main()
