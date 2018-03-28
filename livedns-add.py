#!/usr/bin/env python

import httplib
import json
import os


domain = os.environ.get('CERTBOT_DOMAIN')
challenge = os.environ.get('CERTBOT_VALIDATION')

base_url = "/api/v5/domains/"
conn = httplib.HTTPSConnection("dns.api.gandi.net")

headers= {"X-Api-Key" : "<PUT API KEY>"}
body = {}

conn.request("GET", base_url+domain+"/records/_acme-challenge/TXT", headers=headers)
r1 = conn.getresponse()
if r1.status == 200:
	data = json.loads(r1.read())
	print data
	body["rrset_values"]=[challenge]
	body["rrset_values"]+=data["rrset_values"]
elif r1.status == 404:
	body["rrset_values"]=[challenge]
else:
	print "Error : "+str(r1.status)

conn.close()

headers["Content-Type"] = "application/json"

body["rrset_ttl"] = "300"

print json.dumps(body)

conn.request("PUT", base_url+domain+"/records/_acme-challenge/TXT",body=json.dumps(body), headers=headers)
r1 = conn.getresponse()
print r1.status

conn.close()

