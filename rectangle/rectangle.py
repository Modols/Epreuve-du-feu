import sys

file_1 = sys.argv[1]
file_2 = sys.argv[2]

# print(file_1)
# print(file_2)
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
# print(array)

arrayTest = [s.replace('\n', '') for s in arrayTest]
# print(arrayTest)

# 930870
# 081235
# 973217
# 091230
# 883700
# ['123', '321', '123']

# x=0
# for n in arrayTest:
#     if(array[0] in n):
#         y = n.index(array[0])
#         print("trouvé ", n)

#         if(array[1] in arrayTest[x+1] and len(arrayTest) > x+1):
#             if(y == arrayTest[x+1].index(array[1])):
#                 # print(arrayTest[x+1].index(array[1]))
#                 print("find", arrayTest[x+1])
#                 if(array[2] in arrayTest[x+2] and len(arrayTest) >= x+2):
#                     if(y == arrayTest[x+2].index(array[2])):
#                         print(arrayTest[x+1].index(array[1]))
#                         # print("find", arrayTest[])
#     x+=1

# print(len(arrayTest))

# print(len(array[2]))
# print(arrayTest[2][2:])

# x = arrayTest[2][2:][:len(array[1])]

# print(x)


for x in range(len(arrayTest)):
    if(array[0] in arrayTest[x]):
        y = arrayTest[x].index(array[0])
        # print("trouvé ", arrayTest[x][y:][:len(array[1])], "index : ", y)

        if(array[1] in arrayTest[x+1] and len(arrayTest) > x+1):
            if(y == arrayTest[x+1].index(array[1])):
                # print("find", arrayTest[x+1])
                if(array[2] in arrayTest[x+2] and len(arrayTest) >= x+2):
                    if(y == arrayTest[x+2].index(array[2])):
                        # print(arrayTest[x+1].index(array[1]))
                        print('position : x = ', x, " y = ", y) 
                        break
                        # print("find", arrayTest[])