import sys
import numpy as np

# chaine = list(sys.argv[1])
file_1 = sys.argv[1]

array = []

f1 = open(file_1, "r")
for x in f1:
    if("+" in x):
        continue
    x = x.split("|")
    x= [s.replace('\n', '') for s in x]
    array.append(x)
f1.close()

# print(np.array(array))

def findNumber(tab, x, y, index):
    array= []
    tabTransi = []
    resultX = []
    resultY = []

    tabTransi = list("".join(tab[x]))
    for ix in tabTransi:
        if(ix != "_"):
            array.append(int(ix))
    array.sort()
    
    
    for i in range(1, 10):
        if i not in array:
            resultX.append(i)
    
    tabTransi = []
    for u in range(len(tab)):
        if(tab[u] != tab[x]):
            if(tab[u][y][index] != "_"):
                tabTransi.append(int(tab[u][y][index]))
    tabTransi.sort()
    for i in range(1, 10):
        if i not in tabTransi:
            resultY.append(i)

    for i in resultX:
        if i in resultY:
            return i

for g in range(len(array)):
    for p in range(len(array[g])):
        if("_" in array[g][p]):
            for s in range(len(array[g][p])):
                if(array[g][p][s] == "_"):
                    index = array[g][p].index("_")
                    array[g][p][index]
                    remplace = findNumber(array, g, p, index)
                    array[g][p] = (array[g][p].replace("_", str(remplace), 1))
                   





print(np.array(array))





# ['195' '784' '266']
# ['386' '529' '147']
# ['472' '163' '985']
# ['637' '852' '419']
# ['859' '641' '732']
# ['214' '397' '658']
# ['923' '418' '576']
# ['548' '976' '321']
# ['761' '235' '894']



# 195|784|263
# 386|529|147
# 472|163|985
# ---+---+---
# 637|852|419
# 859|641|732
# 214|397|658
# ---+---+---
# 923|418|576
# 548|976|321
# 761|235|894