#!/usr/bin/python3
# 1-write_file.py
# Alsabti ghaida
"""Module for writing text to a UTF-8 file."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and returns the number of characters written."""

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)