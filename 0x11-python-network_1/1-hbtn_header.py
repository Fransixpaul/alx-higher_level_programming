#!/usr/bin/python3
"""
This module sends a request to a given URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

def main():
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.getheaders()

        headers_dict = dict(headers)

        print(headers_dict.get('X-Request-Id'))

if __name__ == "__main__":
    main()
