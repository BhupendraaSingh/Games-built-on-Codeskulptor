
#Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    else:
        return 4
    



def number_to_name(number):

    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    else:
        return "scissors"


def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    print ("  ")
    
    player_num = name_to_number(player_choice)
    
    comp_num = random.randrange(0,5)
    comp_choice = number_to_name(comp_num)
    
    diff = (comp_num - player_num) % 5
    
    # Gives the decision who wins   
    if (diff == 1) or (diff == 2):
        print ('Player chooses ', player_choice)
        print ('Computer chooses ' ,comp_choice)
        print ("Computer wins!")
       
        
    elif (diff == 3) or (diff == 4):
        print ('Player chooses ', player_choice)
        print ('Computer chooses ' ,comp_choice)
        print ("Player wins!")
        
    # for tie   
    else:
        print ('Player chooses ', player_choice)
        print ('Computer chooses ' ,comp_choice)
        print ("Player and computer tie!")
           
    
        
        

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
