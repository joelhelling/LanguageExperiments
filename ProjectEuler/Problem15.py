import time;
def factorial(n):
	fact = 1;
	for i in xrange(2,n + 1):
		fact *= i;
	return fact;
	
def main():
	print(factorial(40) / (factorial(20) * (factorial(40 - 20))));

start = time.time();
main();
print(time.time() - start);
