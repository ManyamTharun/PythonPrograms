def countdigits(n):
	count = 0
	if n == 0:
		return 1
	else:
		while n > 0:
			n = n // 10
			count = count + 1
		return count
	
n = int(input("Enter a number: "))
print("The no of digits in {} are {}".format(n,countdigits(n)))

	
