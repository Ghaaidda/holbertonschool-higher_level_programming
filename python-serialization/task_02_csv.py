#!/usr/bin/env python3
"""Module for converting CSV data to JSON."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to a JSON file.

    Args:
        csv_filename (str): The name of the CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False