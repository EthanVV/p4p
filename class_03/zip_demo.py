names = ['Alice', 'Bob', 'Charles', 'David']
ages = [18, 17, 25, 22]
schools = ['Stanford', 'Berkeley', 'UCSC', 'SJST']

result = list(zip(names, ages, schools))
print(result)

for name, age, school in zip(names, ages, schools):
  print('Record:', name, age, school)
  print('-'*80)

#
before = [10, 9, 6, 4]
after = [15, 13, 8, 10]

result = [a-b for a, b in zip(after, before)]
print(result)
