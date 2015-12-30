import time;
class PowerOfTwo(object):
	def __init__(self):
		self.digits = [2];
		
	def sum_of_digits(self):
		return sum(self.digits);
		
	def mul_by_two(self):
		self.digits = [x+x for x in self.digits];
		self._add_carry();
		
	def _add_carry(self):
		for i in xrange(0,len(self.digits),1):
			index = len(self.digits) - i - 1;
			if index == 0:
				if self.digits[index] >= 10:
					self.digits[index] -= 10;
					self.digits.insert(0,1);
			else:
				if self.digits[index] >= 10:
					self.digits[index] -= 10;
					self.digits[index-1] += 1;
		
	def print_digits(self):
		print(self.digits);

def main():
	num = PowerOfTwo();
	for i in xrange(1,1000):
		num.mul_by_two();
	num.print_digits();
	print(num.sum_of_digits());

start = time.time();
main();
print(time.time() - start);