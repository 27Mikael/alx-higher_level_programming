#!/bin/bash
# Script sends request to URL and displays size of response
curl -s "$1" | wc -c
