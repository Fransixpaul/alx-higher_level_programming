#!/usr/bin/python3
"""
Main function to authenticate using GitHub API with Basic Authentication
and display the user ID.
"""
import sys
import requests


def main():
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, password))

    if response.status_code >= 200 and response.status_code < 300:
        user_info = response.json()
        print(f"User ID: {user_info['id']}")
    else:
        print(f"Failed to authenticate: {response.status_code}")


if __name__ == '__main__':
    main()
