def get_number(prompt):
    '''Returns integer value for input. Prompt is displayed text'''
    return int(input(prompt))
    
    
def is_prime(number):
    '''Returns True for prime numbers, False otherwise'''
    #Edge Cases
    if number == 1:
        prime = False
    elif number == 2:
        prime = True
    #All other primes    
    else:
        prime = True
        for check_number in range(2, (number / 2)+1):
            if number % check_number == 0:
                prime = False
                break
    return prime

def print_prime(number):
    prime = is_prime(number)
    if prime:
        descriptor = ""
    else:
        descriptor = "not "
    print(number," is ", descriptor, "prime.", sep = "", end = "\n\n")
    

    
#never ending loop

while 1 == 1:
    print_prime(get_number("Enter a number to check. Ctl-C to exit."))

	
	
############################################################################


import sys
number = input("Please enter a number" + "\n" + ">>>")
number = int(number)
prime = False #initiate boolean for true false, default false
if number > 0:
    for x in range (2, number - 1): #this range excludes number and 1, both of which number is divisible by
        if number % x != 0: #If number isn't evenly divisible by x, start over with the next one
            continue 
        elif number % x == 0: #If number is evenly divisible by x, it can't be prime
            sys.exit("The number is not prime.")
    sys.exit("The number is prime.") #number wasn't evenly divisible by any x, so it's prime
elif number == 0:
    sys.exit("The number is not prime.") #According to the Google, 0 is not prime
else:#if number is less than 0, the number is not prime (according to the Google).
    sys.exit("The number is not prime.")
	
	
	