#!/usr/bin/python3
"""Python abstract module"""


class VerboseList(list):
    """This VerboseList class is inherited from python list"""

    def append(self, object):
        super().append(object)
        print(f"Added [{object}] to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, value):
        print(f"Removed [{value}] from the list.")
        super().remove(value)

    def pop(self, index=-1):
        print(f"Popped [{self[index]}] from the list.")
        super().pop(index)
