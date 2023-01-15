number = int(input('enter the number, please :'))
x = False
if number == 1 :
    print('the number is not prime')

elif number > 1 :    
    for n in  range(2,number) :
        if (number % n) == 0 :
         x = True   
        break
    if x :
        print(number, 'is not prime')
    else :
        print(number, 'is a prime')  