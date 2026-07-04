#!/usr/bin/env python3
"""Module for serializing and deserializing a custom object using pickle."""

import pickle


class CustomObject:
    """A custom class that can be serialized and deserialized."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file.

        Returns:
            True if successful, None otherwise.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
            return True
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file.

        Returns:
            A CustomObject instance if successful, None otherwise.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError, EOFError, AttributeError):
            return None