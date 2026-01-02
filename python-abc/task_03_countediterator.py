#!/usr/bin/python3
"""Python abstract module"""


class CountedIterator():
    """This is CountedIterator class"""
    def __init__(self, iterator):
        self.iterator = iter(iterator)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        return self.counter
