author: eforman
date: 201809

flight-seat-selector
HB Prep (Python) Project - Program for randomly selecting a seat on a plane based on A-M-W preference

Basic Rules
1) Must choose from three types of seats: window, middle, aisle
2) Every seat has a row # with the three types of seats above.
3) Can only choose 1 seat
4) Can not choose a seat that's already taken
5) When a seat with a row # and letter is chosen, the program ends

Pseudocode the Work Flow
1) Offer open seat and check if the user wants it.
2) If they want it, print the seat map with the spot taken and wish them a good flight.
3) If they don't want it, ask if they want window, middle, or aisle.
(make sure what's offered isn't what was previously offered)
4) If they want it, print the seat map with the spot taken and wish them a good flight.
5) If they don't want it, ask what row they want. 
(make sure what's offered isn't what was previously offered)
6) Offer open seat and check if the user wants it.
7) If they want it, print the seat map with the spot taken and wish them a good flight.

What data do we need to keep track of
1) What seat type and row #s have already been offered and turned down.
