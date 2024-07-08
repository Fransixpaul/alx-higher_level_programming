#!/usr/bin/python3

import sys
import urllib.parse
import urllib.request

"""
 Main function to send a POST request to a given URL with an email
 as a parameter and print the response body decoded in utf-8.
"""


def main():
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    encoded_data = urllib.parse.urlencode(data).encode('utf-8')

    request = urllib.request.Request(url, data=encoded_data)

    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)


if __name__ == '__main__':
    main()
