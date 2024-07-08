#!/usr/bin/python3
"""
Main function to send a request to a given URL
and display the response body.If the HTTP status code is >= 400,
print an error message with the status code.
"""
import sys
import requests


def main():
    url = sys.argv[1]

    response = requests.get.(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == '__main__':
    main()
