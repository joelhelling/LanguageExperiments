import time;

d = {};
def length_of_collatz(n):
	seq = 1;
	while n != 1:
		if n in d:
			return seq + d[n];
		seq += 1;
		if n % 2 == 0:
			n /= 2;
		else:
			n = 3 * n + 1;
	return seq;
	
def main():
	maxCollatz = 0;
	longest = 0;
	collatzNumbers = {};
	for i in xrange(1,1000000):
		length = length_of_collatz(i);
		d[i] = length;
		if length > maxCollatz:
			maxCollatz = length;
			longest = i;
	print(longest);
	print(maxCollatz);

start = time.time();
main();
print(time.time() - start);