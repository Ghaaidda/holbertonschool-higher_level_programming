import requests
import csv
"""
This module contains a function to fetch and print posts from the JSONPlaceholder API.
"""

def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints the status code,
    fetched data as JSON, and the title of each post.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(f"{post['title']}")

def fetch_and_save_posts():
    """
    Fetches all post from JSONPlaceholder, and saves them as a CSV file.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = [post for post in response.json()]
        headers = ['id', 'title', 'body']
        with open ("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
