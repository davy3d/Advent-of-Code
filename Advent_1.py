#!/usr/bin/env python3

filename = "A_1.txt"
i = 1
y = 0
t = 0

with open(filename) as f:
    for line in f:
        line = line.strip()
        line = list(line)
        #print(line)
        #l = len(line)
        #for x in range(l):
        #    y = y+1
        #    gig = line[l-1]
        try:
            for a in range(10):
                try:
                    line.remove('a')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('b')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('c')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('d')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('e')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('f')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('g')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('h')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('i')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('j')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('k')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('l')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('m')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('n')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('o')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('p')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('q')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('r')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('s')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('t')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('u')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('v')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('w')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('x')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('y')
                except:
                    pass
        except:
            pass        

        try:
            for a in range(10):
                try:
                    line.remove('z')
                except:
                    pass
        except:
            pass        

        z = len(line)
        q = line[0]
        p = line[z-1]
        line = q+p
        line = int(line)
        t = t+line
        
        print(line)

print(f"-----------------------------\n{t}")