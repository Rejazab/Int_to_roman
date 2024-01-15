def from_integer_to_roman(number):
	'''
		Transform number from integer to roman

		Arguments:
		number -- the number to return as a roman

		Return:
		the roman value of the number
	'''
	integer_list = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
	roman_list = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']

	index = len(integer_list)-1
	res = ''

	while number:

		div_value = number // integer_list[index]
		number %= integer_list[index]
		char = roman_list[index]
		index -= 1

		res += char*div_value
	return res


