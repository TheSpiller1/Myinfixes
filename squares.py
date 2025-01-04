# To find if a number is a perfect square or not.
def square_finder(n):
    squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]
    numbers = [0, 1, 4, 9, 6]
    last_numbers = [5, 6, 9, 4, 1]
    last_digit = str(n)[len(str(n)) - 1]
    second_last_digit = str(n)[len(str(n)) - 2]
    if int(last_digit) not in numbers:
        return "Your number is not a perfect square"
    v = 0
    a = 0
    first_digit = str(n)[0]
    second_digit = str(n)[1]
    for every_num in squares:
        if every_num <= int(first_digit + second_digit) <= squares[squares.index(every_num) + 1]:
            a = squares.index(every_num)

        if every_num <= int(second_last_digit + last_digit) <= squares[squares.index(every_num) + 1]:
            if int(first_digit + "5") ** 2 < n:
                v = last_numbers.index(int(last_digit)) + 6

            else:
                v = numbers.index(int(last_digit)) + 1

            if int(f"{a}{v}") ** 2 == n:
                return f"Your is number is a perfect square, the square-root is {a}{v}"

    return "Your number is not a perfect square"


print(square_finder(144))


