#!/usr/bin/env python3

filename = "A_2.txt"
r = 12
g = 13
b = 14
t = 0
w = -1
z = 0
tp = 0
i = ''

with open(filename) as f:
    for line in f:
        line = line.strip()
        line = line.split()
        del line[0]
        #str(line)
        #print(line)
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
            
            #print(w)
            tp = line[w]
            tp = int(tp)
            
            w = w+1
            #print(w)
            i = line[w]
            
            if 'blue' in i:
                if b >= tp:
                    z = z+1
            elif 'red' in i:
                if r >= tp:
                    z = z+1
            elif 'green' in i:
                if g >= tp:
                    z = z+1
        print(f"z is {z}")
        print(f"q/2 is {q//2}")
        if z == q//2:
            t = t+n
        print(f"t is {t}")
        z = 0
print(t)