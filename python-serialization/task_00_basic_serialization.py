#!/usr/bin/env python3
"""Basic serialization module."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize a JSON file into a dictionary."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)