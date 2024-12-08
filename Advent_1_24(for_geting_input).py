
filename = "Advent_1_24.txt"
with open(filename) as f:
    with open("Advent_1_24(2).txt", "a+") as f2:
        with open("Advent_1_24(3).txt", "a+") as f3:
            for line in f:
                line = str(line)
                line = line.replace(' ', '')
                print(line)
                #line = int(line)
                f2.write(line[0:5] + ', ')
                f3.write(line[5:10] + ', ')
            f3.close()
        f2.close()
    f.close()
print('done')
