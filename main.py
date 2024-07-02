import random


def main():
    total = 0
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """

    while total <= 100:
        random_number = random.randint(0, 100)
        if total + random_number > 100:
            break
        numbers.append(random_number)
        total += random_number

    numbers.append(random_number)


    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
