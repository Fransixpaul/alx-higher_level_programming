#!/usr/bin/python3
"""
Main function to fetch the status of https://alx-intranet.hbtn.io/status
and display the response body formatted as required.
"""
import requests


def main():
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)

    content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))


if __name__ == '__main__':
    main()
