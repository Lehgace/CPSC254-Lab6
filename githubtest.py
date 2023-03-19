# Joshua Erickson CPSC 254 | Lab 6 | Github Push

import time # for use of sleep() function

numbers = [5,4,3,2,1] # list to hold countdown numbers

for number in numbers: # loop through all numbers
    print(f"{number}...") # format: "X..."
    time.sleep(1) # 1 second delay between each count
print("Blastoff!") # count is finished, launch the rocket!