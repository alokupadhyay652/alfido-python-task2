"""
Python Developer Task 2 - API Integration
Fetch data from a REST API, filter/search it, and handle errors.
API used: JSONPlaceholder (https://jsonplaceholder.typicode.com)
"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10  # seconds


# ---------------------------------------------------------------
# 3. Handling API errors
# ---------------------------------------------------------------
def fetch_data(url):
    """GET a URL and return parsed JSON, or None if anything goes wrong."""
    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()  # raises HTTPError for 4xx / 5xx
        data = response.json()
        print(f"Successfully fetched data from {url}")
        return data
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err} (status {err.response.status_code}) for {url}")
    except requests.exceptions.ConnectionError as err:
        print(f"Connection error: could not connect to {url}")
    except requests.exceptions.Timeout:
        print(f"Timeout error: request timed out for {url}")
    except ValueError:  # JSON decoding problem
        print(f"Error: response from {url} is not valid JSON")
    except requests.exceptions.RequestException as err:
        print(f"Unexpected error: {err} for {url}")
    return None


# ---------------------------------------------------------------
# 1. Fetching data
# ---------------------------------------------------------------
def show_posts(posts, count=3):
    print(f"Total posts fetched: {len(posts)}")
    print(f"\nFirst {count} posts:")
    for i, post in enumerate(posts[:count], start=1):
        print(f"Post {i}:")
        print(f"  ID: {post['id']}")
        print(f"  Title: {post['title'][:50]}...")
        print(f"  Body: {post['body'][:100]}...")
        print("-" * 20)


# ---------------------------------------------------------------
# 2. Filtering / search logic
# ---------------------------------------------------------------
def filter_by_user(posts, user_id):
    return [p for p in posts if p["userId"] == user_id]


def search_by_keyword(posts, keyword):
    keyword = keyword.lower()
    return [
        p for p in posts
        if keyword in p["title"].lower() or keyword in p["body"].lower()
    ]


def show_filtered(results, label):
    print(f"\n{label}: {len(results)} found")
    if not results:
        print("No posts found.")
        return
    print("First 3 results:")
    for i, post in enumerate(results[:3], start=1):
        print(f"Post {i}:")
        print(f"  ID: {post['id']}")
        print(f"  Title: {post['title'][:50]}...")
        print("-" * 20)


def main():
    # Part 1: fetch
    print("=== 1. Fetching data ===")
    posts = fetch_data(f"{BASE_URL}/posts")
    if posts is None:
        print("Could not fetch posts, stopping.")
        return
    show_posts(posts)

    # Part 2: filter + search
    print("\n=== 2. Filtering and searching ===")
    user_id = 1
    show_filtered(filter_by_user(posts, user_id), f"Posts by User ID {user_id}")
    keyword = "qui"
    show_filtered(search_by_keyword(posts, keyword), f"Posts containing '{keyword}'")

    # Part 3: error handling demo
    print("\n=== 3. Error handling demo ===")
    print("\nSuccessful request:")
    post = fetch_data(f"{BASE_URL}/posts/1")
    if post:
        print(f"Fetched single post title: {post['title'][:50]}...")

    print("\nNon-existent resource (expecting 404):")
    fetch_data(f"{BASE_URL}/nonexistent-endpoint")

    print("\nInvalid URL (expecting connection error):")
    fetch_data("http://invalid.url.example/test")

    print("\nNote: raise_for_status() handles 5xx server errors the same way.")


if __name__ == "__main__":
    main()
