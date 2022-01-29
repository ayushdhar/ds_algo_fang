def find_largest_number(number_of_digits, sum_of_digits):
    if sum_of_digits == 0:
        if number_of_digits == 1:
            return [0]
        else:
            return [-1]

    # sum_of_digits is greater than the maximum possible sum.
    if sum_of_digits > 9 * number_of_digits:
        return [-1]
    res = [0] * number_of_digits
    for i in range(number_of_digits):
        if sum_of_digits < 9:
            sum_of_digits -= 9
            res[i] = 9
        else:
            res[i] = sum_of_digits
            sum_of_digits = 0
    return res


print(find_largest_number(3, 6))
