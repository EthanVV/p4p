# An armstrong number is an integer which has the same value as the sum of the
# Nth power of each of its individual digits where N is the armstrong
# number's length
# E.g: 1634 = 1^4 + 6^4 + 3^4 + 4^4


# does not have input validation
def is_armstrong_number(number):
    number_str = str(number)
    armstrong_power = len(number_str)
    armstrong_sum = 0

    for digit_str in number_str:
        digit = int(digit_str)
        armstrong_sum += digit ** armstrong_power
        if armstrong_sum > number:
            return False

    return armstrong_sum == number
