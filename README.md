******Overview******

This Python program and in particular python function is a solution to find out the missing seat ID in the Python Programming Challenge. This challenge has been solved using Python 3.10.4.

******Dependencies******

Python 3
Any code editor that supports Python3

******Additional files and requirements to run the file******

1. Input text file with all boarding passes information saved on your local computer.
2. Path of this input text file

******Steps to run the program******

1. Open the python file in any code editor that supports Python 3.
2. This program takes the boarding pass information (input) directly from the text file. Please replace the path on the second line of the program with the path at        which your input text file is saved on your computer.
3. Save the python file and run the program to get the output.


******Approach******

**find_missing_seat_id() function logic:**
As it is mentioned that the airline uses binary space partitioning and the first seven characters and last three characters depicts the information about seat row and seat column respectively, it is evident that the first seven characters are nothing but seven bit binary numbers and the last three are 3 characters are 3 bit binary numbers.

Replacing the F,B,L and R characters with 0s and 1s will give a binary sequence. The first seven numbers sequence converted into a decimal gives the row number between 0 to 127 and the last three number sequence gives us the column number or seat number in that particular row from 0 to 7.
So, the find_missing_seat_id() function converts each boarding pass into binary sequence to find out its row and column number and find the unique seat id of every boarding pass using the given formula.

**Missing seat ID:**
As the flight is completely full and no seat is empty, the seat ids list collected in the above function will cover every seat in the flight except mine (or missing). So, the number missing in the sequence of all seat IDs is my (or mising) seat ID.

