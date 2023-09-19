def reversestring(str1):
	str2 = ""
	for i in str1:
		str2 = i + str2
	return str2
str1 = input("Enter a string: ")
print("Reversed string is {}".format(reversestring(str1)))