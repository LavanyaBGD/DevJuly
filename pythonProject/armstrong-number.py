def armstrong(num):
    str_num = str(num)
    num_digits = len(str_num)

    sum_of_powers = sum(int(digit) ** num_digits for digit in str_num)
    return sum_of_powers == num
print(armstrong(123))