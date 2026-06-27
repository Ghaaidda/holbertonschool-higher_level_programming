#!/usr/bin/python3
"""
This file contains a class MyList that inherits 
from the built-in list class and adds a method to print the list in sorted order.
"""
class MyList(list):
    """ Class that inherits the attributes references of class list

    Args:
        list: class list

    """

    def print_sorted(self):
        """ Method that prints the sorted list """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
