from random import randint

def key_generator():
    key = []
    for i in range(5):
        key.append(randint(1,8))
    return key

def decrypt(key, tries):
    red = 0
    white = 0
    for i in range(5):
        if key[i] == tries[i]:
            tries[i] = 0
            red += 1
        #print(key[i], tries[i], red) # debug
    for i in range(5):
        if key[i] in tries:
            white += 1
            tries.remove(key[i])
        #print(key, tries,white) #debug
    print(f"{red} bien placé(s) et {white} mal placés.")




turn = 1
key = key_generator()

while turn < 13:
    ask = ""
    good = False
    print(key)
    while good == False:
        ask = input (f"Tour {turn} : ")
        if len(ask)==5 and ask.isdigit():
            tries = list(ask)
            for i in range(5):
                tries[i] = int(tries[i])
            good = True

    if key == tries:
        print("Bravo tu as trouvé")
        sys.exit()
    else:
        decrypt(key,tries)
        
    turn += 1

print("Perdu gros naze !!!!! ;) ")