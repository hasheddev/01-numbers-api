#!/usr/bin/env python3
'''
    Module for utility functions
'''

def digitSum(number):
    """ Calculates the sum of digits in a number """
    sum = 0

    sign = 1

    if number < 0:
        sign = -1

    number = abs(number)

    while number > 0:
        digit = number % 10
        sum += digiit
        number //= 10
    
    return sum * sign

def isArmstrong(number):
    """ checks ia a number is an armstrong number """
    if number < 0:
        return False
    if number == 0 or number == 1:
        return True
    
    sum = 0
    dup = number

    while dup > 0:
        digit = dup % 10
        sum += (digit * digit * digit)
        dup = dup // 10
    
    return sum == number


def isPerfect(number):
    """ Determines if a number is a perfect number """
    if number <= 3:
        return False
    
    divisor_sum = 1
    num = 2

    while ((num * num) <= number):
        if not number % num:
            divisor_sum += (num + ((number // num) if number // num != num else 0))
        num += 1

    return divisor_sum == number

def isPrime(number):
    if number <= 1:
        return False
    
    num = 1
    count = 0
    
    while ((num * num) <= number):
        if number % num == 0:
            count += 1
            if (number // num) != num:
                count += 1
        num += 1
    
    print(count)
    return count == 2
