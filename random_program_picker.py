import random

def choose_random_program():
    """
    :type nums: List[int]
    :rtype: int
    """

    # loop through random numbers until we encounter one that isnt already 
    # contained in the list inside alreadyChosenPrograms.txt
    choice_made = False
    while choice_made is False:

        random_choice = random.randrange(1,76)

        with open("alreadyChosenPrograms.txt") as f:
            for l in f:                
                if (int(l) == random_choice):
                    break
            
            choice_made = True
            number = str(random_choice)

    print("creating new file for program: "+number+"...")

    # adding program number to the list of already chosen programs
    with open("alreadyChosenPrograms.txt", "a") as f:
        f.write(number+"\n")

    # creating a new file for the latest program
    with open("p"+number+".py", "x") as f:
        f.write("# Blind 75 #"+number+"\n")   

choose_random_program()