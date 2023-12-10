#!/usr/bin/env python3

filename = "A_2.txt"
t = 0
w = -1
tp = 0
i = ''
lowestBlue = 0
lowestRed = 0
lowestGreen = 0

with open(filename) as f:
    for line in f:
        lowestBlue = 0
        lowestRed = 0
        lowestGreen = 0
        line = line.strip()
        line = line.split()
        del line[0]
        n = line[0]
        n = n[:-1]
        del line[0]
        print(line)
        n = int(n)
        print(n)
        q = len(line)
        w = -1
        q = int(q)
        for j in range(int(q/2)):
            w = w+1
            
            tp = line[w]
            tp = int(tp)
            
            w = w+1
            i = line[w]
            
            if 'blue' in i:
                if tp > lowestBlue:
                    lowestBlue = tp
                
            elif 'red' in i:
                if tp > lowestRed:
                    lowestRed = tp
                
            elif 'green' in i:
                if tp > lowestGreen:
                    lowestGreen = tp
                
        t = t+lowestBlue*lowestGreen*lowestRed
        print(f"the current total is {t}")
        print(f"lowestBlue is {lowestBlue}, lowestGreen is {lowestGreen}, and lowestRed is {lowestRed}.")
print(f"the total is {t}")