import math
import json

# Constants
SEAT_EMPTY = "."
SEAT_OCCUPIED = "X"
SEAT_RESTRICTED = "e"
FRONT_PRICE = 80
MIDDLE_PRICE = 50
BACK_PRICE = 25
SALES_TAX_RATE = 0.0725
MASK_FEE = 5.0
NUM_ROWS = 20
NUM_COLS = 26

# Initialize seating chart
seating_chart = [[SEAT_EMPTY for j in range(NUM_COLS)] for i in range(NUM_ROWS)]

# Initialize purchase history
purchase_history = []

# Function to display the seating chart
def display_seating_chart():
    print("\n   " + " ".join([chr(65+j) for j in range(NUM_COLS)]))
    for i in range(NUM_ROWS):
        print("{:2d} ".format(i) + " ".join(seating_chart[i]))

# Function to calculate the price of a ticket
def calculate_ticket_price(row):
    if row < 5:
        return FRONT_PRICE
    elif row < 11:
        return MIDDLE_PRICE
    else:
        return BACK_PRICE

# Function to purchase a ticket
def purchase_ticket():
    # Ask for number of tickets to purchase
    while True:
        num_tickets = input("\nHow many tickets would you like to purchase? ")
        if num_tickets.isdigit() and int(num_tickets) > 0:
            num_tickets = int(num_tickets)
            break
        else:
            print("Invalid input. Please enter a positive integer.")

    # Ask for row and column of first seat
    while True:
        seat = input("Enter the row and column of the first seat (e.g., 3A): ")
        if len(seat) == 2 and seat[0].isdigit() and 0 <= int(seat[0]) < NUM_ROWS and seat[1].isalpha() and \
                0 <= ord(seat[1].upper()) - 65 < NUM_COLS:
            row = int(seat[0])
            col = ord(seat[1].upper()) - 65
            if seating_chart[row][col] != SEAT_EMPTY:
                print("Seat is already occupied or restricted due to Covid-19.")
            elif row < 2 or (col >= 2 and seating_chart[row][col-2] == SEAT_OCCUPIED) or \
                    (col <= NUM_COLS-3 and seating_chart[row][col+2] == SEAT_OCCUPIED):
                print("There must be 2 social distancing seats between each occupied seat on a row.")
            else:
                break
        else:
            print("Invalid input. Please enter a valid seat (e.g., 3A).")

    # Reserve seats and calculate total price
    total_price = 0
    seats = []
    for i in range(num_tickets):
        row_str = "{:02d}".format(row)
        col_str = chr(col + 65)
        seat_str = row_str + col_str
        seats.append(seat_str)
        seating_chart[row][col] = SEAT_OCCUPIED
        total_price += calculate_ticket_price(row)
        if col < NUM_COLS-1 and seating_chart[row][col+1] == SEAT_EMPTY:
            col += 1
       
