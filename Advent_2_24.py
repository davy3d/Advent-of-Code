filename = 'Advent_2_24.txt'
a = 0
x = 0
safeRep = 0
b = 0
y = 0
with open(filename) as f:
    for line in f:
        x = 0
        a = 0
        line = line.strip()
        line = line.split()
        #print(line)
        line = list(map(int, line))
        y = len(line)
        #print(y)
        for i in range(len(line)):
            if x < 99999:
                x = 0
            if a == y:
                x = 100000
            while x < y:
                if line[x] + 1 == line[x+1] or line[x] + 2 == line[x+1] or  line[x] + 3 == line[x+1] or line[x] - 1 == line[x+1] or line[x] - 2 == line[x+1] or line[x] - 3 == line[x+1]:
                   a += 1
                else:
                    x += 100000
            
                x += 1
                print(x)
                print(a)
                print(len(line))
        if a == len(line):
            safeRep += 1
        print('safeRep', safeRep)
print(safeRep)
