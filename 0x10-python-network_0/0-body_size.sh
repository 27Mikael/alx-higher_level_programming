#!/bin/bash
# Script sends request to URL and displays size of response
curl -s "$URL" | wc -c
