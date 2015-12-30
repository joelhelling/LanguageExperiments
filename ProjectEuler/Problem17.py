import time;
def get_ones_digit(n):
	count = 0;
	if n == 0:
		print("bad");
		count = 0;
	elif n == 1:
		count = 3;
	elif n == 2:
		count = 3;
	elif n == 3:
		count = 5;
	elif n == 4:
		count = 4;
	elif n == 5:
		count = 4;
	elif n == 6:
		count = 3;
	elif n == 7:
		count = 5;
	elif n == 8:
		count = 5;
	elif n == 9:
		count = 4;
	return count;

def get_tens_digit(n):
	count = 0;
	if n == 2:
		count = 6;
	elif n == 3:
		count = 6;
	elif n == 4:
		count = 5;
	elif n == 5:
		count = 5;
	elif n == 6:
		count = 5;
	elif n == 7:
		count = 7;
	elif n == 8:
		count = 6;
	elif n == 9:
		count = 6;
	return count;

def get_special_tens(n):
	count = 0;
	if n == 10:
		count = 3;
	elif n == 11:
		count = 6;
	elif n == 12:
		count = 6;
	elif n == 13:
		count = 8;
	elif n == 14:
		count = 8;
	elif n == 15:
		count = 7;
	elif n == 16:
		count = 7;
	elif n == 17:
		count = 9;
	elif n == 18:
		count = 8;
	elif n == 19:
		count = 8;
	if count == 0:
		print("oops");
	return count;

def get_letter_count(n):
	count = 0;
	length = len(str(n));
	if length == 1:
		count += get_ones_digit(n);
	elif length == 2:
		if n < 20:
			count += get_special_tens(n);
		else:
			count += get_ones_digit(n%10);
			count += get_tens_digit(int(n/10))
	elif length == 3:
		count = 10;
		lastDigits = n % 100;
		if lastDigits < 10:
			count += get_ones_digit(lastDigits);
		elif lastDigits < 20:
			count += get_special_tens(lastDigits);
		else:
			count += get_ones_digit(lastDigits%10);
			count += get_tens_digit(int(lastDigits/10));
		count += get_ones_digit(int(n/100));
	else:
		count = 11;
	return count;

def main():
	sum = 0;
	for i in xrange(1,1001):
		print("num ", i);
		print("count ", get_letter_count(i));
		sum += get_letter_count(i);
		print("total ", sum);
	print(sum);

start = time.time();
main();
print(time.time() - start);