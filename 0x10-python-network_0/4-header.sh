#!/bin/bash
# Send a GET request to a URL and display the body of the response
curl -sL -H 'X-HolbertonSchool-User-Id: 98' -- "$1"
