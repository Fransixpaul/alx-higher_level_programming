#!/bin/bash
# send request to URL and display only the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
