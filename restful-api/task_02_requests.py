#!/usr/bin/python3
import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    API-dən post-ları alır,
    status code-u və bütün title-ları çap edir
    """
    response = requests.get(URL)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    API-dən post-ları alır və
    id, title, body sahələri ilə CSV faylına yazır
    """
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        structured_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "title", "body"]
            )
            writer.writeheader()
            writer.writerows(structured_posts)