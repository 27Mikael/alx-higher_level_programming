#!/bin/bash
#Displays all methods an HTTP server will accept
curl -sI "$1" | grep "Allow:" | cut -d " " -f 2-
