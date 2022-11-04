import random

number = random.randint(0,10)
thresh = 5

print(number)

if(number > thresh):
    print('Big Number')
elif(number < thresh):
    print('Small Number')
elif(number > thresh + 2):
    print('Really Big Number')
elif(number == thresh):
    print('Number is', str(thresh))
    
if(number > thresh + 2):
    print('Really Big Number')
    
    