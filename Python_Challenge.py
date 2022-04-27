#Importing the contents of our text file into a list using the path at which the input text file is saved.
with open(r"C:\Users\gundimed\Downloads\input.txt",'r') as f:
    input = f.read().splitlines()

#This function finds out maximum and missing seat IDs using the list of Boarding Passes and prints them as output. Also, this function returns the missing seat ID.
def find_missing_seat_id(input):

    #Initialise empty seat_ids lists to collect all seat ids calculated from boarding passes
    seat_ids = []
    missing_list=[]

    #Loop to read each boarding pass from the list
    for boarding_pass in input:

        #Convert the F and B, and L and R into binary language by replacing them with 0s and 1s
        #Replacing F with 0, B with 1, L with 0, R with 1
        translation_table = boarding_pass.maketrans("FBLR", "0101")
        
        #Convert the boarding pass sequence into binary sequence with 1s and 0s
        test = boarding_pass.translate(translation_table)
        test = list(test)

        #Using the first 7 characters of the boarding pass to get row information
        row = ''.join(test[:7])
        row = int(row,2)

        #Using the last 3 characters of the boarding pass to get column information
        column = ''.join(test[7:])
        column = int(column,2)

        #Calculate the seat id using row and column number of the boarding pass
        seat_id = (row*8)+column
        seat_ids.append(seat_id)
    
    #Arranging the boarding passes into ascending order
    seat_ids.sort()
    
    #Print out the maximum Seat ID
    print("Maximum Seat ID is: " + str(seat_ids[-1]))
    
    #Loop to find the missing seat (ID) between first and last available seats (IDs)
    for i in range(seat_ids[0],seat_ids[-1]+1):
        if i not in seat_ids:
            missing_list.append(i)

    #Print out the missing/my Seat ID
    print("My Seat ID is: " + str(missing_list[0]))

    return missing_list[0]

#Function call
find_missing_seat_id(input)
