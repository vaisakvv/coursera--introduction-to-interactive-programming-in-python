
# The key idea of this program is to equate the strings

# "rock", "paper", "scissors", "lizard", "Spock" to numbers

# as follows:

#

# 0 - rock

# 1 - Spock

# 2 - paper

# 3 - lizard

# 4 - scissors

import random

def name_to_number(name):

    if name== 'rock':

        return 0

    elif name=='Spock':

        return 1

    elif name=='paper':

        return 2

    elif name=='lizard':

        return 3

    elif name=='scissors':

        return 4

    else:

        print "Invalid name"


def number_to_name(number):

    if number==0:

        return 'rock'

    elif number==1:

        return 'Spock'

    elif number==2:

        return 'paper'

    elif number==3:

        return 'lizard'

    elif number==4:

        return 'scissors'

    else:

        print 'Invalid choice'

        

def rpsls(player_choice): 
     
    if not(player_choice == 'rock' or player_choice == 'Spock' or player_choice=='paper' or player_choice=='lizard' or player_choice=='scissors'):
        print "Invalid input \n"
    else:
        print 'Player chooses',player_choice

        player_number=name_to_number(player_choice)

        comp_number=random.randrange(0,4)

        comp_choice=number_to_name(comp_number)

        print "Computer chooses ",comp_choice
    
        if comp_number-player_number==0:
            print "Game tie..."
        elif (comp_number-player_number)%5 <=2:
            print "Computer wins !!"
        else:
            print "Player wins !!"
        print "\n"
    
    

rpsls("rock")

rpsls("Spock")

rpsls("paper")

rpsls("lizard")

rpsls("scissors")



# always remember to check your completed program against the grading rubric




