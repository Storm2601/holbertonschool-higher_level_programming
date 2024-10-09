#!/usr/bin/env python3

import csv  # Import the csv module for handling CSV file operations
import requests  # Import the requests module to make HTTP requests


def fetch_and_print_posts():
    """
    Fetches posts from a RESTful API and prints their titles.

    This function sends a GET request to the specified API
    endpoint and retrieves a list of posts. It then prints
    the title of each post.

    Args:
        None

    Returns:
        None
    """
    # Send a GET request to the API endpoint to fetch posts
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # Print the status code of the response
    print(f"Status Code: {response.status_code}")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response into a list of posts
        posts = response.json()
        # Iterate through each post and print its title
        for post in posts:
            print(post['title'])  # Print the title of the current post


def fetch_and_save_posts():
    """
    Fetches posts from the given API endpoint and saves them to a CSV file.

    This function sends a GET request to the API endpoint
    "https://jsonplaceholder.typicode.com/posts" to retrieve
    a list of posts. It then extracts the necessary information
    from each post and saves it to a CSV file named "posts.csv"
    with the columns 'id', 'title', and 'body'.

    Returns:
        None
    """
    # Send a GET request to fetch posts from the API
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response into a list of posts
        posts = response.json()
        # Create a list of dictionaries containing relevant post data
        post_list = [{'id': post['id'], 'title': post['title'],
                      'body': post['body']} for post in posts]

        # Define the name of the CSV file to save the posts
        csv_file = 'posts.csv'
        # Open the CSV file in write mode with UTF-8 encoding
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            # Create a CSV DictWriter object for writing dictionaries to the CSV
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            # Write the header row to the CSV file
            writer.writeheader()
            # Write the list of posts to the CSV file
            writer.writerows(post_list)
