import math

def get_digits(num):
	digits = []
	while(num > 0):
		digit = num%10
		digits.append(digit)
		num /= 10
	return digits
		
def sum_of_fifth_powers(digits):
	sum = 0
	for digit in digits:
		sum += pow(digit,5)
	return sum
	
powers_match = []
for i in range(2,1000000):
	if i == sum_of_fifth_powers(get_digits(i)):
		powers_match.append(i)

print(sum(powers_match))