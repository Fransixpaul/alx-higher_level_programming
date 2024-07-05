#!/bin/bash
# Send POST request with variables to URL and display the body of the response
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
