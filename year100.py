# Request age
# Request how many copies of message to print
# Print year they will turn 100

from datetime import datetime 

def inputInteger(prompt):
    while True:
        try:
            value = int(raw_input(prompt)) # Do not use input in python 2.7, as it uses eval() under the covers...
            break
        except ValueError:
            print("Please input a valid integer.")
            
    return value

age = inputInteger("How old will you be this year?: ")

copies = inputInteger("How many copies of the message do you want to print?: ")

year_turn_100 = 100 - age + datetime.now().year
if age < 100:
    print ("You will turn 100 in the year %d.\n" % year_turn_100) * copies
else:
    print ("You turned 100 in the year %d.\n" % year_turn_100) * copies
    