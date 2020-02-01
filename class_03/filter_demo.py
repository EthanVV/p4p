# filter out odd numbers
numbers = [0, 8, 9, 4, 1, 3]
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(even_numbers)

# filter out words with a length less than 8
text = 'Or kind rest bred with am shed then. In raptures building an bringing be. Elderly is detract tedious assured private so to visited.'
length_threshold = 8
long_words = list(filter(lambda word: len(word) >= length_threshold, text.split()))

print(long_words)

# filter out numbers on excluded list
numbers = [5, 30, 20, 12, 9, 8, 19, 4]
exludes = [9, 12, 8, 4, 17, 32]

result = list(filter(lambda number: number not in exludes, numbers))
print(result)

# filter out numbers that are odd then square the reamaning items
numbers = [0, 8, 9, 4, 1, 3]

squared_even_numbers = list(
  map(
    lambda even_number: even_number ** 2,
    filter(lambda number: number % 2 == 0, numbers)
    )
  )

print(squared_even_numbers)