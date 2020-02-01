# numbers = [9, 3, 6, 1]

# square_numbers = [number**2 for number in numbers]
# print(square_numbers)

# numbers = [0, 8, 9, 4, 1, 3]
# squared_even_numbers = [number**2 for number in numbers if % 2 == 0]
# print(squared_even_numbers)

emails = ['alice 12@gmail.com', 'alice123', 'bob@abc.com', 'alice@gmail.com']
valid_emails = [email for email in emails if ' ' not in email and '@' in email]
print(valid_emails)

# numbers = [0, 8, 9, 4, 1, 3],
# result = [0 if number % 2 == 0 else 1 for number in numbers]
# print(results)