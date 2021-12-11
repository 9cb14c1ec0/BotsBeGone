#!/usr/bin/python3
import os
import json
import ipaddress

data_path = '/var/lib/BotsBeGone'
os.system(f'/bin/git -C {os.path.join(data_path, "git")} pull origin')

with open(os.path.join(data_path, 'BotsBeGone', 'ip_addresses.json')) as new_file:
    new_data = json.loads(new_file)

with open(os.path.join(data_path, 'local', 'ip_addresses.json')) as old_file:
    old_data = json.loads(old_file)

new_addresses = []
removed_addresses = []

# new ip addresses
for ip_address in new_data:
    if ip_address not in old_data:
        # roundtrip through the ipaddress library to prevent command injections in case of source repository compromise
        i = str(ipaddress.ip_address(ip_address))
        os.system(f'ufw prepend deny from {i}')

# ip addresses to delete
for ip_address in old_data:
    if ip_address not in new_data:
        i = str(ipaddress.ip_address(ip_address))
        os.system(f'ufw delete deny from {i}')

# save new_data as old
with open(os.path.join(data_path, 'local', 'ip_addresses.json'), 'w') as local_file:
    json.dumps(new_data)
