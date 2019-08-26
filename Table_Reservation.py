"""
Tung Hoang - 08/26/19

This program asks user to input a name and check if they have a reservation.
If they do, invite them in. If not, say they do not have reservations.
"""

# The name constant
rightName = "Tung"

# Ask user for input
reservationName = input("Name: ")

# Check if it is the right name
if reservationName == rightName:
    print ("Right this way!")
else:
    print ("Sorry, we don't have a reservation under that name.")
