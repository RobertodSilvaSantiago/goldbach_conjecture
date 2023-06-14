import math


def get_even_number() -> int:
    """ Prompt the user to enter a natural even number greater than 2.

    Returns:
        int: The natural even number entered by the user.

    """

    while True:
        even_number_str = input('Enter a natural even number greater than 2: ')
        try:
            even_number = int(even_number_str)
            if even_number > 2 and even_number % 2 == 0:
                return even_number
        except ValueError:
            pass
        print('Error: please enter a valid natural even number greater than 2.')


def get_pairs_of_primes(number: int) -> list:
    """ Find all pairs of primes that sum up to the given even number.

    Args:
        number (int): The even number to find pairs of primes for.

    Returns:
        list: A list of tuples, where each tuple contains a pair of primes that sum up to the given number.

    """

    pairs = []

    if number % 2 == 1:
        return pairs

    for first_prime in range(2, number):
        if is_prime(first_prime):
            for second_prime in range(first_prime, number - first_prime + 1):
                if is_prime(second_prime) and first_prime + second_prime == number:
                    pairs.append((first_prime, second_prime))
    return pairs


def is_prime(number: int) -> bool:
    """ Check if a number is a prime.

    Args:
        number (int): The number to check for prime number.

    Returns:
        bool: True if the number is prime, False otherwise.

    """

    if number < 2:
        return False
    max_factor = int(math.sqrt(number)) + 1
    for factor in range(2, max_factor):
        if number % factor == 0:
            return False
    return True


def main():
    """ Find all pairs of primes that sum up to a user-entered even number."""

    number = get_even_number()
    pairs = get_pairs_of_primes(number)
    for pair in pairs:
        print(f"The number {number} equals to the sum of {pair[0]} and {pair[1]}")


if __name__ == "__main__":
    main()