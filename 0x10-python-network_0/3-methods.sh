#!/bin/bash
#Displays all methods an HTTP server will accept
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2-