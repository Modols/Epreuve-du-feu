import sys

file_1 = sys.argv[1]
file_2 = sys.argv[2]

array = []
arrayTest = []

f1 = open(file_1, "r")
for x in f1:
  array.append(x)
f1.close()

f2 = open(file_2, "r")
for x in f2:
    arrayTest.append(x)
f2.close()

array = [s.replace('\n', '') for s in array]

arrayTest = [s.replace('\n', '') for s in arrayTest]

for x in range(len(arrayTest)):
    if(array[0] in arrayTest[x]):
        y = arrayTest[x].index(array[0])
        if(array[1] in arrayTest[x+1] and len(arrayTest) > x+1):
            if(y == arrayTest[x+1].index(array[1])):
                if(array[2] in arrayTest[x+2] and len(arrayTest) >= x+2):
                    if(y == arrayTest[x+2].index(array[2])):
                        print('position : x = ', x, " y = ", y) 
                        break