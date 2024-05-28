
def sum_numbers(number):
    if number < 0:
        number = abs(number)
    if number <= 9:
        return number
    else: 
        return number % 10 + sum_numbers(number // 10)