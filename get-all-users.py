#!/usr/bin/env python3
import requests
from zuliprc import auth, baseurl

response = requests.get(f"{baseurl}/api/v1/users", auth=auth)
print(response.text)
