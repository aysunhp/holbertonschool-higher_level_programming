#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in roman_string:
        result += roman_nums[i]
    return result
