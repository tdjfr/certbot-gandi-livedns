#!/usr/bin/env python

import httplib
import json
import os


domain = os.environ.get('CERTBOT_DOMAIN')
challenge = os.environ.get('CERTBOT_VALIDATION')

base_url = "/api/v5/domains/"
conn = httplib.HTTPSConnection("dns.api.gandi.net")

headers= {"X-Api-Key" : "<PUT API KEY>"}
headers["Content-Type"] = "application/json"

conn.request("DELETE", base_url+domain+"/records/_acme-challenge/TXT", headers=headers)
r1 = conn.getresponse()
conn.close()

