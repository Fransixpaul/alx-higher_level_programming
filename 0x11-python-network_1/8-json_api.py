#!/usr/bin/python3
"""
Main function to send a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter and process the response.
"""
import sys
import requests


def main():
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {'q': q}

    response = requests.post(url, data=data)

    try:
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")


if __name__ == '__main__':
    main()
