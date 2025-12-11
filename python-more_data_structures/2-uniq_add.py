#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqes = set(my_list)
    result = 0
    for i in uniqes:
        result += i
    return result
