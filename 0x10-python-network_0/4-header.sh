#!/bin/bash
# Send GET request with custom header to URL and display the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
