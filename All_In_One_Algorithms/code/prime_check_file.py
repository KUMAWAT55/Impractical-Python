'''code to check whether a number is prime or not '''
import math
def prime_check(number):
    '''Function Implemented '''
    if number % 2 == 0 and number > 2:
        return False
    return all(number % i for i in range(3, int(math.sqrt(number))+1, 2))
