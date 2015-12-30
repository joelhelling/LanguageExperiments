def get_abundant_numbers():
    abundant = []
    for i in range(12,28123+1):
        sum = 1
        for j in range(2,int(i/2)+1):
            if i % j == 0:
                sum += j
        if sum > i:
            abundant.append(i)
    return abundant

def main():
    abundant = get_abundant_numbers()
    print(abundant)
    print(len(abundant))


main()
