# certbot-gandi-livedns
Python script to manage Gandi LiveDNS and wildcard certificat

This script can manage certificat with wildcard and domain certificat like
*.domain.tld and domain.tld

Use these script :
./certbot-auto certonly -manual-public-ip-logging-ok --manual --manual-auth-hook livedns-add.py --manual-cleanup-hook livedns-delete.py -d '*.domain.tld' -d 'domain.tld' --preferred-challenges dns

