import math
num1 = int(input('Please Enter the First Number: '))
num2 = int(input('Please Enter the Second Number: '))
print (f'{num1} rounded up is {math.ceil(num1)}. {num1} rounded down is {math.floor(num1)}.')
print (f'The Value of {num1} After Copying the Sign from {num2} is {math.copysign(num1, num2)}.')
print (f'The Absolute Value of {num1} is {math.fabs(num1)}.')
print (f'The GCD of {num1} and {num2} is {math.gcd(num1, num2)}.')