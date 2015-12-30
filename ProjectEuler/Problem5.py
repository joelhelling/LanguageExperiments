def gcd(a,b):
	while b:
		a,b = b, a%b;
	return a;

def lcm(a,b):
	return a * b / gcd(a,b);

def main():
	i = reduce(lcm,range(1,21));
	print(i);

main();
#232792560