import time


# Converts binary to decimal
def binary_to_dec(binary_num):
    try:
        return int(binary_num, 2)
    except ValueError:
        return 0


# Checks primes
def is_prime(n):
    # Will sort out the numbers less than 2
    if n < 2:
        return False
    if n in (2, 3):
        return True
    # Gets rid of even numbers and multiples of 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Checks any numbers that are larger than 3
    limit = int(n ** 0.5) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


# filters primes from a list of numbers
def get_prime_list(list_of_denary, given_integer):
    return [num for num in list_of_denary if num < given_integer and is_prime(num)]

#This will print the prime numbers
def print_prime_list(prime_list):
    n = len(prime_list)
    if n > 0:
        first_three = prime_list[:3]
        last_three = prime_list[-3:] if n >= 3 else prime_list  # Ensures correct slicing

        print(f"{n}:")
        print(f"{', '.join(map(str, first_three))}")
        print(f"{', '.join(map(str, last_three))}")
    else:
        print("None")

# converts binary input to a list of binary digits
def binary_list(binary):
    return [i for i in binary if i in '01']


def binary_substrings(list_of_binary):
    # Gets substrings of various sizes
    return list({"".join(list_of_binary[i:j]) for i in range(len(list_of_binary)) for j in
                 range(i + 1, len(list_of_binary) + 1)})


# Converts binary to decimal
def get_dec_list(list_of_values):
    return sorted({binary_to_dec(i) for i in list_of_values})


# Binary string input
#test 1
#binary = '0100001101001111'
#given_integer = 999999
# #test 2
# binary = '01000011010011110100110101010000'
# given_integer = 999999
# #test 3
# binary = '1111111111111111111111111111111111111111'
# given_integer = 999999
# #test 4
# binary = '010000110100111101001101010100000011000100111000'
# given_integer = 999999999
# #test 5
binary = '01000011010011110100110101010000001100010011100000110001'
given_integer = 123456789012
# #test 6
# binary = '0100001101001111010011010101000000110001001110000011000100111001'
# given_integer = 123456789012345
# #test 7
# binary = '010000110100111101001101010100000011000100111000001100010011100100100001'
# given_integer = 123456789012345678
# #test 8
# binary = '01000011010011110100110101010000001100010011100000110001001110010010000101000001'
# given_integer = 1234567890123456789
# #test 9
# binary = '0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100'
# given_integer = 1234567890123456789
# #test 10
# binary = '010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011'
# given_integer = 12345678901234567890
# #handritten test 1
# binary = '101101'
# given_integer = 7
# #handwritten test 2
# binary = '101010011101'
# given_integer = 234
# #handwritten test 3
# binary = '111001100101011'
# given_integer = 10000
# #handwritten test 4
# binary = '100011010101110'
# given_integer = 7000
# #handwritten test 5
# binary = '110010101110011011'
# given_integer = 12000


start =  time.time()
# Extracts primes
prime_numbers = get_prime_list(get_dec_list(binary_substrings(binary_list(binary))), int(given_integer))

# Output
print_prime_list(prime_numbers)
end = time.time()
print("Time:", end - start)