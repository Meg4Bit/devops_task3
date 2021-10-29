#!/usr/bin/python3

import sys
import datetime
import os


sys.stdout.write("Content-Type: text/html\r\n\r\n")
sys.stdout.write("<h1>Hello from Python Script!</h1>\r\n\r\n")


sys.stdout.write("<p>Current data (UTC): ")
datetime_object = datetime.datetime.now()
print(datetime_object)
sys.stdout.write("</p>")

sys.stdout.write("<p>Browser fingerprint: ")
print(os.environ.get('HTTP_USER_AGENT', ''))
sys.stdout.write("</p>")
