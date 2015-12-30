import math;
def is_palindrome(n):
	length = get_length(n);
	digits = [];
	while n > 0:
		digits.append(n%10);
		n /= 10;
	
	palindrome = True;
	for i in range(int(len(digits) / 2)):
		if digits[i] != digits[len(digits) - 1 - i]:
			palindrome = False;
			break;
	
	return palindrome;

def get_length(n):
	return int(math.log10(n)) + 1;
	
def main():
	numOne = 999;
	numTwo = 999;
	largest = False;
	while numOne > 99:
		while numTwo > 989:
			if is_palindrome(numOne * numTwo):
				largest = True;
				break;
			numTwo -= 1;
		if largest:
			break;
		numOne -= 1;
		numTwo = 999;
	print(numOne*numTwo);

main();