#!/bin/bash
#Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
[ "$(curl -s -o response_body.txt -w "%{http_code}" "$1")" -eq 200 ]
