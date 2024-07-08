#!/usr/bin/python3
"""
Main function to send a POST request to a given URL with
an email as a parameter and print the response body.
"""
import sys
import requests


def main():
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    response = requests.post(url, data=data)

    print(response.text)


if __name__ == '__main__':
    main()
