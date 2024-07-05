#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# send a request to the URL and capure the response body
response=$(curl -s "$1")

status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")
echo "HTTP status code: $status_code"

headers=$(curl -s -D - "$1" -o /dev/null)
echo "Response headers: $headers"

echo "Response body: '$Response'"

# Displays the size of the response body in bytes
echo -n "$response" | wc -c
