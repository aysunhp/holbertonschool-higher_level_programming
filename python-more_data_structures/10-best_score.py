#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary.values():
       return max(a_dictionary.values())
    else:
        return None
