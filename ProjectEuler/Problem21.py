import time;
import math;
def divisor_sum(num):
    sum = 0;
    maxDivisor = int(math.sqrt(num));
    for i in xrange(1,num / 2 + 1):
        if num % i == 0:
            sum += i;

    return sum;

def main():
    sum = 0;
    for i in xrange(2,10001,2):
        possible =  divisor_sum(i);
        if i == divisor_sum(possible):
            if i != possible:
                sum += i;
    print(sum);

start = time.time();
main();
print(time.time() - start);
