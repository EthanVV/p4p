#fout = open('names.txt', 'w')
#fout.write('Alice\n')
#fout.write('Bob\n')

fin = open('names.txt')

line = fin.readline()

while line:
    line = (fin.readline()).strip()
    if not line:
        break
    print(len(line))
    print(line)


fin.close()