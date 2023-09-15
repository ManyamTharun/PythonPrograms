""" Strong number is a special number whose sum of the factorial of digits is equal to the original number. For Example: 145 is strong number. Since, 1! + 4! + 5!"""

def factorial(x):
    fact = 1
    for i in range(1, x+1):
        fact *= i
    return fact
n = int(input("Enter Number: "))
temp = n
summ =0
while n > 0:
        rem = n%10
        summ += factorial(rem)
        n = n//10
if summ == temp:
    print("TRUE")
else:
    print("FALSE")
