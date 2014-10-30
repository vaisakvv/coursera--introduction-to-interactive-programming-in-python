#go to this link to run the code
#http://www.codeskulptor.org/#user38_ZZEl15nqbP_0.py
# template for "Guess the number" mini-project

# input will come from buttons and an input field

# all output for the game will be printed in the console

import simplegui,random

attempts,count,secretno=0,0,0



# helper function to start and restart the game

def new_game():

    print 'New game...'

    print 'Select the number range.'

def range100():

    global secretno,attempts,count

    secretno=random.randrange(0,100)

    attempts,count=0,7

    print 'New Game.. Range is from 0 to 100'

    
#Buttons
def range1000():

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

    
# create frame

frame = simplegui.create_frame("Guess the number", 100,200, 100)

# register event handlers for control elements and start frame

frame.add_button("Range: 0-100", range100, 100)

frame.add_button("Range: 0-1000", range1000, 100)

frame.add_input("Enter guess:", input_guess, 100)


# call new_game 

new_game()


frame.start()
