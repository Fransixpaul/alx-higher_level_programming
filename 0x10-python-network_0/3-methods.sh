#!/bin/bash
# Send OPTIONS request to URL and display allowed HTTP methods
curl -sI "$1" | grep "Allow:" | cut -d' ' -f2-
