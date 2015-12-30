def main():
	even = 0;
	fib = [1,1];
	while fib[len(fib)-1] < 4000000:
		next = fib[len(fib) - 1] + fib[len(fib) - 2];
		if next % 2 == 0:
			even += next;
		fib.append(next);
	print(even);
	
main();