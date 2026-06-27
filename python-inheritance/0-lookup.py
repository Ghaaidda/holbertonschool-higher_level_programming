#!/usr/bin/python3
# 0-lookup.py
# Alsabti ghaida <13216@holbertstudenst.com>
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
    