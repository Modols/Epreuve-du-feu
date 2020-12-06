import sys

result = int(sys.argv[1])

def fact(total, number):
    if(number == 1):
        return total
    else:
        total *= (number-1)
        return fact(total, (number-1))

print(fact(result, result))