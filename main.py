import random
import time
from plane_map import plane_map 


#Project_test

def prints_greeting():
    #Prints the Introductory Greeting
    print("Alaska Airlines acquired Virgin America in 2016.")

    time.sleep(2)

    print("\nSince then, Sir Richard Branson has been counting the grains of sand on Necker Island, his private hideaway in the Caribbean.")

    time.sleep(3)

    print("\nIt's taken him two years, but he's nearly done counting, and he's ready to launch his next airline.")

    #ef: url?
    time.sleep(3)

    print("\nYou've been chosen as one of the lucky few to take the inaugural flight.")

    time.sleep(3)

def flyer_ready():
    #Returns if they're ready to fly
    while True:
        travel_choice = input("\nAre you ready for takeoff? [Y/N]").upper()
        
        if travel_choice not in ["Y","N"]:
            print ("\nThat's not an option. Let's try this again.")
            True
        elif travel_choice == "N":
            print("\nBack to counting sand for Richard. \n\nEnd of Program")
            return(travel_choice)
        elif travel_choice == "Y":
            print("\nGreat!")
            return(travel_choice)
            
def seat_col(choose_to_fly,seat_columns):
    #Returns seat column (e.g.wind,mid,ais)
    while True:
        print("\nWould you like a seat in the:\n")

        for key in seat_columns:
            print ("[",key,"]",seat_columns[key])

        seat_col_choice = input("\nEnter here>").upper()
        
        if seat_col_choice not in seat_columns:
            print("\nThat's not an option. Let's try this again.")
        else:
            break
            #ef check if there are open seats, if so:
    return (seat_col_choice)

def seat_row_generator(max_row,offered_rows,seat_type):

    while True:

        row = random.randint(1,max_row+1) 

        if row not in offered_rows:
            break
        elif row in offered_rows and seat_type not in offered_rows[row]:
            break

    return row

def seat_row(seat_col,seat_columns,max_row,offered_row):

    #and check for seats that are already taken
    
    print("\nYou're in luck! We have an open",seat_columns[seat_col],f'seat. It\'s in row {offered_row}.\n')

    time.sleep(2)

    plane = plane_map(max_row,offered_row,seat_col)

    for i in plane:
        print(i,plane[i])

def seat_row_work(row):
    while True:
        print("\nWould you like to:\n\n[1] Select this seat \n[2] Roll the dice again")
        #\n[3] Choose a specific seat from the map

        works = input("\nEnter here>")

        if works not in ("1","2","3"):
            print("\nThat's not an option. Let's try this again.")
        else:
            break

    return works
    
        #based on the seat column, select a random seat number and ask if it works for them.
def print_boarding_pass(seat_type,offered_row):
    print(f'\nYou\'re ready for takeoff!\n\nPrint your boarding pass:\n\nRow: {offered_row}  Seat: {seat_type}\n\n<<Save to Apple wallet>>')

######################################################

#variables
seat_columns = {"W":"Window", "M":"Middle", "A":"Aisle"}
max_row = 30
offered_rows = {}

def run_seat_picker():
    """Runs seat picker"""
    prints_greeting()
    choose_to_fly = flyer_ready()
    while choose_to_fly == "Y":

        seat_type = seat_col(choose_to_fly, seat_columns)

        offered_row = seat_row_generator(max_row,offered_rows, seat_type)

        if offered_row in offered_rows:
            offered_rows[offered_row].append(seat_type)
        else:
            offered_rows[offered_row] = [seat_type]

        #print (offered_rows)

        seat_row_num = seat_row(seat_type, seat_columns,max_row,offered_row)

        row_works = seat_row_work(seat_row_num)
        
        if row_works == "2":
            #print(offered_rows)
            continue
        #elif row_works == "3":
                    #row and seat equals user inputs
            
        print_boarding_pass(seat_type,offered_row)
        break
    # playing = True
    # while playing:
        # get user's birth information
        # generate horoscope
        # print horoscope
        # ask to continue

run_seat_picker()

###########################################
#Basic Rules
#1) Must choose from three types of seats: window, middle, aisle
#2) Every seat has a row # with the three types of seats above.
#3) Can only choose 1 seat
#4) Can not choose a seat that's already taken
#5) When a seat with a row # and letter is chosen, the program ends

# Pseudocode the Work Flow
# Offer open seat and check if the user wants it.
# If they want it, print the seat map with the spot taken and wish them a good flight.
# If they don't want it, ask if they want window, middle, or aisle.
#(make sure what's offered isn't what was previously offered)
# If they want it, print the seat map with the spot taken and wish them a good flight.
#If they don't want it, ask what row they want. 
#(make sure what's offered isn't what was previously offered)
# Offer open seat and check if the user wants it.
# If they want it, print the seat map with the spot taken and wish them a good flight.


# What data do we need to keep track of
# 1) What seat type and row #s have already been offered and turned down.