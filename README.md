# goldbach_conjecture

This code is a Python program that prompts the user to enter a natural even number greater than 2. It then finds all pairs of prime numbers that sum up to the given even number and displays the pairs to the user.

The program consists of several functions:

get_even_number(): This function repeatedly prompts the user to enter a natural even number greater than 2 until a valid input is provided. It returns the entered even number.

get_pairs_of_primes(number): This function takes an even number as input and finds all pairs of prime numbers that sum up to the given number. It iterates through possible values of the first prime number and checks if the second prime number, when added to the first, equals the given number. It returns a list of tuples, where each tuple represents a pair of primes that satisfy the condition.

is_prime(number): This function checks whether a number is prime. It iterates from 2 to the square root of the number and checks if any of these values evenly divide the number. If such a factor is found, the function returns False; otherwise, it returns True.

main(): This function serves as the entry point of the program. It calls get_even_number() to obtain an even number from the user, then calls get_pairs_of_primes(number) to find the pairs of primes that sum up to the given number. Finally, it displays the pairs to the user.

The program imports the math module for performing square root calculations.

By executing the code, the user can interact with the program to find pairs of primes that sum up to a given even number
