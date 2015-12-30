import time;
def nth_triangle_number(n):
	return sum(xrange(1,n+1));

def number_of_divisors(n):
	divs = 2;
	for i in range(2,int(n**0.5) + 1):
		if n % i == 0:
			if i*i < n:
				divs += 2;
			else:
				divs += 1;
	return divs;
	
def main():
	num = 0;
	for i in xrange(1,100000000):
		num = i*(i+1)/2;
		divs = number_of_divisors(num);
		if divs > 500:
			break;
	print(num);

startTime = time.time();
main();
print(time.time() - startTime);