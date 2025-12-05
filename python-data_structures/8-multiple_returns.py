#!/usr/bin/python3
def multiple_returns(sentence):
    a1 = len(sentence)
    a2 = sentence[0] if len(sentence) > 0 else None
    return (a1, a2)
