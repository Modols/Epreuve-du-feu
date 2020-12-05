import sys

def writeLine(total, i):
    total_blanc = total-i
    s = ""
    for x in range(total_blanc ):
        s += " "
    for y in range(i):
        s += "#"
    print(s)

for i in range(1 ,int(sys.argv[1]) +1):
    writeLine(int(sys.argv[1]), i)