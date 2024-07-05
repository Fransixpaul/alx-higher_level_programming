#!/bin/bash
# Send JSON POST request to URL with JSON data from file and display the body of the response
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
