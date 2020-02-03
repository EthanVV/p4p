def calculate(a, b, c):
  return a + b**2, c**3

print(calculate(1, 2, 3))
print(calculate(c=3, b=2, a=1))

def mystery(a, b, *c):
  return 10*a, 5*b, sum(c)

print(mystery(1, 2, 3, 4, 5, 6,))