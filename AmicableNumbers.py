"""Amicable numbers are two different natural numbers related in such a way that the sum of the proper divisors of each is equal to the other number.Ex:(220,284), (1184,1210)"""

def FactorsSum(x):
    summ = 0
    for i in range(1, x):
        if x%i == 0:
            summ += i
    return summ
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
summ1 = FactorsSum(n1)
summ2 = FactorsSum(n2)
# print(summ1, summ2)
if summ1 == n2 and summ2 == n1:
    print("{} and {} are Ammicable numbers".format(n1, n2))
else:
             print("{} and {} are not Ammicable numbers".format(n1, n2))
            
