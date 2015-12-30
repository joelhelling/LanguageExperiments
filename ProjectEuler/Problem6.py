def main():
	sumOfSquare = 0;
	squareOfSum = 0;
	
	for i in range(1,101):
		sumOfSquare += i*i;
		squareOfSum += i;
	
	squareOfSum *= squareOfSum;

	print(squareOfSum - sumOfSquare);
	
main();