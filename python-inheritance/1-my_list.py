#!/usr/bin/python3
# 1-my_list.py
# Alsabti ghaida <13216@holbertstudenst.com>
"""Defines a class MyList that inherits from class List."""

class MyList(List):
    """Class MyList definition."""
    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))

