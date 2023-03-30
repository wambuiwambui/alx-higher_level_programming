#!/bin/bash

# Check if argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <url>"
  exit 1
fi

# Send request and save response headers to a temporary file
curl -s -o /tmp/headers.txt -w "%{http_code}" "$1"

# Extract status code from the headers file and display it
cat /tmp/headers.txt

# Remove temporary file
rm /tmp/headers.txt
