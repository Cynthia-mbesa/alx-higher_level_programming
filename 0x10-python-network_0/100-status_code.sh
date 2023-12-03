#!/bin/bash
# sends a request to argument(URL), and displays only the status code of the response
curl -L -s -X HEAD -w "%{http_code}" "$1"
