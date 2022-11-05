# EC2 Random Name Generator

# Python libraries

import random
import string
import time

# Function to generate random names.

def random_ID(size=12, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))

'''Input block
Enter Accounting, FinOps, or Marketing
*** CASE SENSITIVE ***'''

department = input("Enter Department:  ")

for _ in department:
    if department == "Accounting":
        print("...Please Wait... ")
        time.sleep(3)
        print("The name generator is checking credentials...")
        time.sleep(3)
        break
    elif department == "FinOps":
        print("...Please Wait... ")
        time.sleep(3)
        print("The name generator is checking credentials...")
        time.sleep(3)
        break
    elif department == "Marketing":
        print("...Please Wait... ")
        time.sleep(3)
        print("The name generator is checking credentials...")
        time.sleep(3)
        break
    else:
        print("*Access Denied* :-(  Please check for errors and re-enter...")
        time.sleep(3)
        department = input("Enter Department:  ")
        time.sleep(3)
number = int(input("Enter Qty of Name Request(s): "))

# Print result
print("...Please wait...")
time.sleep(3)
print("*** Today\'s your lucky day! :-) *** You win New Instance Name(s):")
time.sleep(3)

for _ in range(1, number + 1):
    EC2_name = department
    New_ID_name = EC2_name + "-" + random_ID()
    print("New name:", New_ID_name)

# Thanks for stopping by!


