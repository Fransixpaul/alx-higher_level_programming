#!/usr/bin/python3
"""
Main function to send a GET request to a given URL and print the response body
decoded in utf-8. If an HTTPError occurs, print the error code.
"""
import sys
import urllib.request
import urllib.error


def main():
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == '__main__':
    main()
