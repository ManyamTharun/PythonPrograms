def FactorsSum(x):
    summ = 0
    for i in range(1, x):
        if x%i == 0:
            summ += i
    return summ
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
lst = []
for i in range(n1, n2 + 1):
    if i == FactorsSum(i):
        lst.append(i)
print("The perfect numbers in range of {} and {} are {}".format(n1, n2, lst))
    
