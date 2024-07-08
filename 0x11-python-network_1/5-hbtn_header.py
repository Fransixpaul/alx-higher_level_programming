#!/usr/bin/python3
"""
Main function to send a request to a given URL and display the value of
the variable X-Request-Id found in the response header
"""
import sys
import requests


def main():
    url = sys.argv[1]

    response = requests.get(url)

    x_request_id = response.headers.get('X-Request-Id')

    print(x_request_id)


if __name__ == '__main__':
    main()
