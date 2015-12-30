import math;
def main():
	primes = [];
	for i in range(2,114319):
		isPrime = True;
		for j in primes:
			if i % j == 0:
				isPrime = False;
				break;
		if isPrime:
			primes.append(i);
				
	print(primes[10000]);

main();