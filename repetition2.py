import random

for i in range(0, 5):
    print(i)
    
number = random.randint(0, 100)

thresh = 17
counter = 0

#print('Number equals', number)

while(number != thresh):
    counter += 1
    number = random.randint(0,100)
    
    if(counter > 100):
        print('I\'m BROKEN!!!')
        break
    
    
    print('Number equals', number)
    print('Threshold equals', thresh)
    print('Number of attempts', counter)
  #And that's how we do it!  
