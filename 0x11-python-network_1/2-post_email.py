#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)

The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
"""
from urllib.request import Request, urlopen
import sys
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    req = Request(
            url,
            data=data,
            headers={
                'User-Agent': 'Mozilla/6.0'
                }
            )
    with urlopen(req) as response:
        print(response.read().decode("utf-8"))
