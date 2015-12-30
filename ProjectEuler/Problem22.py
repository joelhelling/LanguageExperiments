def calc_alpha_value(name):
    sum = 0
    for c in name:
        sum += ord(c) - ord('A') + 1
    return sum

def calc_name_score(i,name):
    return i * calc_alpha_value(name.upper())

def main():
    with open("p022_names.txt") as nameInput:
        names = nameInput.read()
    names = names.split(',')
    for i in range(0,len(names)):
        names[i] = names[i].strip('"')
    names.sort()
    sum = 0
    for i in range(1,len(names)+1):
        sum += calc_name_score(i,names[i-1])
    print(sum)

main()
