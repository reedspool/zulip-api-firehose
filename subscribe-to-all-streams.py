#!/usr/bin/env python3
import requests
import json
from zuliprc import auth, baseurl

streams_response = requests.get(f"{baseurl}/api/v1/streams",
                        auth=auth)
streams = streams_response.json()['streams']

streams_names_only = [{ "name": d['name'] } for d in streams]

# You can limit just to one for safe testing
# streams_names_only = [{ "name": "wizardcity" }]

subscribe_response = requests.post(f"{baseurl}/api/v1/users/me/subscriptions",
                                   auth=auth,
                                   data={"subscriptions": json.dumps(streams_names_only)})
