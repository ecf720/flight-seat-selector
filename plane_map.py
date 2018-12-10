import random
plane = {}
#max_row = 30
#customer_row = 14
#customer_seat = "W"

def plane_map(max_row,customer_row,customer_seat):

    #half of rows will have booked seats
    booked_seats = random.sample(range(1,max_row), int(max_row/2)) 

    for i in range(1,max_row):
        #zfill to standardized indents for single-char digits
        i = int(str(i).zfill(2))

        if i in booked_seats:
            if i%2 == 0:
                plane[i] = "_|X|_"
            elif i%3 == 0:
                plane[i] = "X|X|X"
            else:
                plane[i] = "X|_|X"
        else:
            plane[i] = "_|_|_"

    #customer seat
    customer_row = int(str(customer_row).zfill(2))
    
    if customer_seat == "W":
        plane[customer_row] = "W|_|_"
    elif customer_seat == "M":
        plane[customer_row] = "_|M|_"
    elif customer_seat == "A":
        plane[customer_row] = "_|_|A"

    return plane

#plane = plane_map(max_row,customer_row,customer_seat)
#for i in plane:
    #print(i,plane[i])



        