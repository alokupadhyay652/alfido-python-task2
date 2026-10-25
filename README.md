# alfido-python-task2

Alfido Tech Python Developer Internship - Task 2: API Integration & JSON Handling

## About
A small Python project that fetches data from a REST API, filters and searches it, and handles errors safely. It uses the free JSONPlaceholder API (https://jsonplaceholder.typicode.com).

## What it does
1. Fetch data: sends a GET request to /posts using the requests library, parses the JSON response and prints the first 3 posts.
2. Filter and search: filters posts by userId, and searches posts by a keyword in the title or body.
3. Error handling: handles HTTP errors (404, 5xx), connection errors, timeouts and invalid JSON without crashing.

## How to run
```
pip install requests
python main.py
```

## Output
- Total posts fetched: 100
- Posts by User ID 1: 10 found
- Posts containing 'qui': 89 found
- A 404 error and a connection error are caught and printed cleanly.

## Concepts used
requests.get, status codes, raise_for_status(), try/except, list comprehensions, timeouts.

## Repository
https://github.com/alokupadhyay652/alfido-python-task2

## Document
https://drive.google.com/file/d/1ipWZn_aOGCiT5gMQUF3y4TvSphgcCNd9/view?usp=drivesdk
