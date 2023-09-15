def FactorsSum(x):
    summ = 0
    for i in range(1, x):
        if x%i == 0:
            summ += i
    return summ
n = int(input("Enter a number: "))
summ1 = FactorsSum(n)
if summ1 == n:
    print("The number({}) and sum of its proper divisors({}) are equal".format(n, summ1))
else:
    print("The number({}) and sum of its proper divisors({}) are not equal".format(n, summ1))
