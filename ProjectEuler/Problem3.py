def main():
	n = 600851475143;
	factors = [];
	d = 2;
	while n > 1:
		while n % d == 0:
			print("adding ", d ," to the list");
			factors.append(d);
			n /= d;
		d = d + 1;
		if d*d > n:
			if n > 1: 
				factors.append(n);
			break;
	print(factors);
	print(max(factors));
	
main();