def fibonacci(n):
	n1 = 0
	n2 = 1
	if n <= 0:
		print("Invalid Number")
	elif n == 1:
		print(n1)
	else:
		print("The Fibonacci Series containing {} terms is".format(n))
		print(n1,n2,end = " ")
		for i in range(2,n):
			nxt_num = n1 + n2
			n1 = n2
			n2 = nxt_num
			print(nxt_num,end = " ")
n = int(input("Enter the no of terms in Fibonacci Series: "))
fibonacci(n)