def Armstrong(num):
	length = len(str(num))
	summ = 0
	while num > 0:
		# Accessing each digit from number
		digit = num % 10
		summ = summ + digit ** length
		# Removing a digit 
		num = num // 10
	return summ
num = int(input("Enter a number: "))
if Armstrong(num) == num:
		print("{} is an Armstrong number.".format(num))
else:
		print("{} is not an Armstrong number.".format(num))
		
		