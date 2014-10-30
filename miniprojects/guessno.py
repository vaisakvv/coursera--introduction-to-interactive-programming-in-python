http://www.codeskulptor.org/#user38_ZZEl15nqbP_0.py
# template for "Guess the number" mini-project

# input will come from buttons and an input field

# all output for the game will be printed in the console

import simplegui,random

attempts,count,secretno=0,0,0



# helper function to start and restart the game

def new_game():

    # initialize global variables used in your code here



    # remove this when you add your code    

    print 'New game...'

    print 'Select the number range.'



# define event handlers for control panel

def range100():

    # button that changes the range to [0,100) and starts a new game 

    

    # remove this when you add your code    

    global secretno,attempts,count

    secretno=random.randrange(0,100)

    attempts,count=0,7

    print 'New Game.. Range is from 0 to 100'

    

def range1000():

    # button that changes the range to [0,1000) and starts a new game     

    global attempts,secretno,count

    attempts,count=0,10

    secretno=random.randrange(0,1000)

    print 'New Game... Range is from 0 to 1000'

    

    

def input_guess(guess):

    global secretno,attempts,count

    guess=int(guess)

    attempts+=1

    count-=1

    print 'Guessed number is %d'%guess

    if guess == secretno:

        print 'Correct... You guessed the number in %d attempts \n'%attempts

    elif guess<secretno:

        print 'Secretnumber is higher and %d attempts left\n'%count

    elif count==0:

        print 'Game over...You Lost..Secretnumber is %d\n'%secretno

        new_game()

    else:

        print 'Secretnumber is lower and %d attemts left\n'%count

        # main game logic goes here	

    

    # remove this when you add your code

    



    

# create frame

frame = simplegui.create_frame("Guess the number", 100,200, 100)





# register event handlers for control elements and start frame

frame.add_button("Range: 0-100", range100, 100)

frame.add_button("Range: 0-1000", range1000, 100)

frame.add_input("Enter guess:", input_guess, 100)





# call new_game 

new_game()



frame.start()

# always remember to check your completed program against the grading rubric
