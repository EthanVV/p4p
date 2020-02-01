def is_self_divisor(number):
    number_str = str(number)
    for digit_str in str(number_str):
        digit = int(digit_str)
        if digit == 0 or number % digit != 0:
            return False

    return True


self_divisor_count = 0
floor = 1
ciel = 2001

for i in range(floor, ciel):
    if is_self_divisor(i):
        self_divisor_count += 1
        print(i)
