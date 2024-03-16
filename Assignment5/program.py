#
# Write the implementation for A5 in this file
#

import random
from math import sqrt

# TODO for A5: A8 B9
'''
 Use functions to: read a complex number from the console, write a complex number to the console,
 implement each required functionality.
 Functions communicate using input parameter(s) and the return statement (DO NOT use global variables,
 nested functions, the global or nonlocal keywords)
 Have two separate representations for each complex number, one using a list and another using a dictionary.
 Write methods to create a new complex number, to get and set each number's real and imaginary parts as well as to
 transform a number into its str representation. The program must work with both implementations, by either commenting
 out one of them or changing the order in which the corresponding functions are defined.
 Separate input/output functions (those using print and input statements) from those performing the calculations
 (see program.py)
 Provide the user with a menu-driven console-based user interface. Input data should be read from the console and
 the results printed to the console. At each step, the program must provide the user the context of the operation
 (do not display an empty prompt).
'''



# 
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
#
# def create_complex_number(real, imaginary):
#     '''
#     Creates a complex number in list representation
#     :param real: the real part of the complex number
#     :param imaginary: the imaginary part of the complex number
#     :return: a complex number in list representation
#     '''
#     return [real, imaginary]
#
# def get_real(complex_number):
#     return complex_number[0]
#
# def get_imaginary(complex_number):
#     return complex_number[1]
#
# def set_real(complex_number, new_real):
#     complex_number[0] = new_real
#
# def set_imaginary(complex_number, new_imaginary):
#     complex_number[1] = new_imaginary
#
# def to_string(complex_number):
#     if complex_number[0] == 0:
#         if complex_number[1] == 0:
#             return "0"
#         else:
#             return str(complex_number[1]) + "i"
#     if complex_number[1] == 0:
#         return str(complex_number[0])
#     if complex_number[1] > 0:
#         return str(complex_number[0]) + "+" + str(complex_number[1]) + "i"
#     else:
#         return str(complex_number[0]) + str(complex_number[1]) + "i"

#
# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

def create_complex_number(real, imaginary):
    '''
    Creates a complex number in dict representation
    :param real: the real part of the complex number
    :param imaginary: the imaginary part of the complex number
    :return: a complex number in dict representation
    '''
    return {'real': real, 'imaginary': imaginary}

def get_real(complex_number):
    return complex_number['real']

def get_imaginary(complex_number):
    return complex_number['imaginary']

def set_real(complex_number, new_real):
    complex_number['real'] = new_real

def set_imaginary(complex_number, new_imaginary):
    complex_number['imaginary'] = new_imaginary

def to_string(complex_number):
    if complex_number['real'] == 0:
        if complex_number['imaginary'] == 0:
            return "0"
        else:
            return str(complex_number['imaginary']) + "i"
    if complex_number['imaginary'] == 0:
        return str(complex_number['real'])
    if complex_number['imaginary'] > 0:
        return str(complex_number['real']) + "+" + str(complex_number['imaginary']) + "i"
    else:
        return str(complex_number['real']) + str(complex_number['imaginary']) + "i"

def generate_random_complex_numbers():
    """
    Generates 10 random complex numbers
    :return:
    """
    complex_numbers = []
    for i in range(10):
        real = random.randint(-100, 100)
        imaginary = random.randint(-100, 100)
        complex_numbers.append(create_complex_number(real, imaginary))
    return complex_numbers


#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

'''
Set A
8. Length and elements of a longest subarray of numbers where both their real and imaginary parts can be written 
using the same base 10 digits (e.g. 1+3i, 31i, 33+i, 111, 11-313i)
Set B
9. The length and elements of a longest increasing subsequence, when considering each number's modulus
'''

def is_same_base_10_digits(cNr1, cNr2):
    '''
    Checks if two complex numbers have the same base 10 digits
    :param cNr1: the first complex number
    :param cNr2: the second complex number
    :return: True if the two complex numbers have the same base 10 digits, False otherwise
    '''
    digits1 = [0] * 10
    digits2 = [0] * 10
    real1 = abs(get_real(cNr1))
    imaginary1 = abs(get_imaginary(cNr1))
    real2 = abs(get_real(cNr2))
    imaginary2 = abs(get_imaginary(cNr2))

    while real1 != 0:
        digits1[real1 % 10] = 1
        real1 //= 10
    while imaginary1 != 0:
        digits1[imaginary1 % 10] = 1
        imaginary1 //= 10

    while real2 != 0:
        digits2[real2 % 10] = 1
        real2 //= 10
    while imaginary2 != 0:
        digits2[imaginary2 % 10] = 1
        imaginary2 //= 10

    for i in range(10):
        if digits1[i] != digits2[i]:
            return False
    return True

def modulus(complex_number):
    '''
    Gets the modulus of a complex number
    :param complex_number: the complex number
    :return: the modulus of the complex number
    '''
    val = sqrt(get_real(complex_number) ** 2 + get_imaginary(complex_number) ** 2)
    return val

def is_increasing(complex_number1, complex_number2):
    '''
    Checks if a complex number is increasing
    :param complex_number1: the first complex number
    :param complex_number2: the second complex number
    :return: True if the first complex number is increasing, False otherwise
    '''
    return modulus(complex_number1) < modulus(complex_number2)

def is_increasing_subsequence(complex_numbers):
    '''
    Checks if a list of complex numbers is increasing
    :param complex_numbers: the list of complex numbers
    :return: True if the list of complex numbers is increasing, False otherwise
    '''
    for i in range(len(complex_numbers) - 1):
        if not is_increasing(complex_numbers[i], complex_numbers[i + 1]):
            return False
    return True

def get_longest_subarray_same_base_10_digits(complex_numbers):
    '''
    Gets the longest subarray of numbers where both their real and imaginary parts can be written using the same base 10 digits
    :param complex_numbers: the list of complex numbers
    :return: the longest subarray of numbers where both their real and imaginary parts can be written using the same base 10 digits
    '''
    longest_subarray = []
    current_length = 1
    current_subarray = []
    for i in range(len(complex_numbers) - 1):
        if current_length == 1:
            current_subarray = [complex_numbers[i]]
        if is_same_base_10_digits(complex_numbers[i], complex_numbers[i + 1]):
            current_length += 1
            current_subarray.append(complex_numbers[i + 1])
        else:
            if current_length > len(longest_subarray):
                longest_subarray = current_subarray
            current_length = 1
            current_subarray = []

    if current_length > len(longest_subarray):
        longest_subarray = current_subarray

    return longest_subarray

def longest_increasing_modulus_subsequence(complex_nums):
    n = len(complex_nums)
    dp = [1] * n  # Initialize all elements with a minimum sequence length of 1
    prev = [-1] * n  # To store the previous index for reconstructing the subsequence

    for i in range(1, n):
        for j in range(i):
            if modulus(complex_nums[i]) > modulus(complex_nums[j]) and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_len = max(dp)
    end_index = dp.index(max_len)

    # Reconstruct the subsequence
    subsequence = []
    while end_index != -1:
        subsequence.append(complex_nums[end_index])
        end_index = prev[end_index]

    return max_len, subsequence[::-1]  # Reverse the subsequence to get the correct order



#
# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#

def read_complex():
    real = int(input("Enter the real part: "))
    imaginary = int(input("Enter the imaginary part: "))
    return real, imaginary

def write_complex(complex_num):
    print(to_string(complex_num))

def read_list_of_complex_numbers():
    '''
    Reads a list of complex numbers from the console
    :return: a list of complex numbers
    '''
    complex_numbers = []
    number_of_complex_numbers = int(input("Enter the number of complex numbers: "))
    for i in range(number_of_complex_numbers):
        real, imaginary = read_complex()
        complex_numbers.append(create_complex_number(real, imaginary))
    return complex_numbers

def print_complex_numbers(complex_numbers):
    '''
    Prints a list of complex numbers
    :param complex_numbers: the list of complex numbers
    :return: None
    '''
    for complex_number in complex_numbers:
        print(to_string(complex_number))


'''
    
Implement a menu-driven console application that provides the following functionalities:

Read a list of complex numbers (in z = a + bi form) from the console.
Display the entire list of numbers on the console.
Display on the console the sequence, subarray or numbers required by the properties that were assigned 
to you. Each student will receive one property from Set A and another one from Set B.
Exit the application.

'''

def print_menu():
    print("1. Read a list of complex numbers from the console")
    print("2. Display the entire list of numbers on the console")
    print("3A. Display the length and elements of a longest subarray of numbers where both their real and imaginary parts can be written using the same base 10 digits")
    print("3B. Display the length and elements of a longest increasing subsequence, when considering each number's modulus")
    print("0. Exit the application")


if __name__ == "__main__":
    complex_numbers = []
    complex_numbers = generate_random_complex_numbers()
    while True:
        print_menu()
        option = input("Enter your option: ")
        if option == "1":
            complex_numbers = complex_numbers + read_list_of_complex_numbers()
        elif option == "2":
            print_complex_numbers(complex_numbers)
        elif option == "3A":
            print_complex_numbers(get_longest_subarray_same_base_10_digits(complex_numbers))
        elif option == "3B":
            length, subsequence = longest_increasing_modulus_subsequence(complex_numbers)
            print("The length of the longest increasing subsequence is: " + str(length))
            print_complex_numbers(subsequence)
        elif option == "0":
            break
        else:
            print("Invalid option!")




