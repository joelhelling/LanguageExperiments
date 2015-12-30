import time;
def main():
	fact = 1;
	for i in range(1,101):
		fact *= i;
	
	sum = 0;
	while fact > 0:
		sum += int(fact%10);
		fact = int(fact/10);
	print(sum);

start = time.time();
main();
print(time.time() - start);