#!/bin/bash
# takes in a URLand Display only body of a 200 status code response
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -Ls "$1"; fi
