#!/bin/bash
# sends a JSON POST request to first argument(Url), and displays the body of the response.
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
