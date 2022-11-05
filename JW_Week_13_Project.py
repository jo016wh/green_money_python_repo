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

print("Enter: Accounting, FinOps, or Marketing")
department = input("Enter Department:  ")

for _ in department:
    if department == "Accounting" or department.lower() == "accounting":
        print("...Please Wait... ")
        time.sleep(3)
        print("The name generator is checking credentials...")
        time.sleep(3)
        break
    elif department == "FinOps" or department.lower() == "finops":
        print("...Please Wait... ")
        time.sleep(3)
        print("The name generator is checking credentials...")
        time.sleep(3)
        break
    elif department == "Marketing" or department.lower() == "marketing":
        print("...Please Wait... ")
        time.sleep(3)
        print("The name generator is checking credentials...\n")
        time.sleep(3)
        break
    else:
        print("🚨🚨🚨 ACCESS DENIED! 🚨🚨🚨 😲  Please check for errors and re-enter...")
        time.sleep(3)
        department = input("Enter Department:  ")
        time.sleep(3)
number = int(input("Enter Qty of Name Request(s): "))

# Print result
print("\n...Please wait...\n")
time.sleep(3)
print("🎊  Today\'s your lucky day! 🎊 \n😁  You win New Instance Name(s)!:")
time.sleep(3)

for _ in range(1, number + 1):
    EC2_name = department
    New_ID_name = EC2_name + "-" + random_ID()
    print("\nNew name:", New_ID_name)
    
print("\n💥Thanks for visiting John's name generator Python Project!!!💥")





