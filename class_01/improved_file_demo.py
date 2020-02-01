with open('names.txt') as fin, open('names_upper.txt', 'w') as fout:
    for line in fin:
        name = line.strip()
        #fout.write(name.upper() + ' ' + str(len(name)) + '\n')
        fout.write('{} {}\n'.format(name.upper(), len(name)))