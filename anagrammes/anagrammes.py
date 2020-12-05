import sys

chaine = list(sys.argv[1])
file_1 = sys.argv[2]

array = []
f1 = open("fr.txt", "r")
for x in f1:
  array.append(x)
f1.close()

array = [s.replace('\n', '') for s in array]

resultArray = []

for i in array:
  y = list(i)
  # print(i)
  check = all(item in chaine for item in y)
  if (check is True):
    resultArray.append(i)

print(resultArray)