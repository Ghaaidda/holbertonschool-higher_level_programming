#!/usr/bin/python3
"""Module for appending text to a UTF-8 file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF-8 text file.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
        