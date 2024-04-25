import re

def find_rabbit(filename):
    counter = 0
    with open(filename) as file:
        for line in file:
            line.strip()
            if re.findall("rabbit", line.lower()):
                #print(line)
                counter += len(re.findall("rabbit", line.lower()))
    return counter

def power(base, exponent):
    if exponent < 0:
        return "Undefined"
    elif exponent == 0:
        return 1
    elif exponent == 1:
        return base
    elif (exponent % 2) == 1:
        return base * power(base, exponent // 2) * power(base, exponent // 2)
    else:
        return power(base, exponent // 2) * power(base, exponent // 2)

def main():
    print(find_rabbit("../data/alice.txt"))
    print(power(4, 7))

if __name__ == "__main__":
    main()