import sys

chaine = list(sys.argv[1])

for charac in range(len(chaine)):
    
    if (chaine[charac] == " " ):
        pass
    elif ( charac % 2 == 0 ):
        chaine[charac] = chaine[charac].lower()
    else:
        chaine[charac] = chaine[charac].upper()

print("".join(chaine))