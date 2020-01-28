#!/usr/bin/env python3
import sys, random #imports sys (system) and random library

assert sys.version_info >= (3,7), "This script requires at least Python 3.7" #version of python currently being used


print('Greetings friend!') #prints greetings! to the screen
colors = ['red','orange','yellow','green','blue','violet','purple'] #string assortment that can be picked
play_again = '' #awaiting user input for there are four possible answers y,n,yes,no
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'): #answe n and no from user input are being used
    match_color = random.choice(colors) #rand choice of "color"
    count = 0 #zero attempts made yet
    color = '' #awaiting user input for color
    while (color != match_color): #color will be the answer but which
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() #spelling aid
        count += 1 #bump up attempt when one is made
        if (color == match_color): #answer is correct
            print('Correct!') #print cprrect!
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #if wrong print statement and show guess from guesses=count
    
    print('\nYou guessed it in {} tries!'.format(count)) #shows attempts when correct

    if (count < best_count): #if count is lower than "highscore"
        print('This was your best guess so far!') #print statement
        best_count = count #set count to current best count

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() #play again with print statement awaiting user input and has typo forgiveness

print('Thanks for playing!') #print statement