#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# send a request to the URL and capure the response body
response=$(curl -s "$1")

# Displays the size of the response body in bytes
echo -n "$response" | wc -c
