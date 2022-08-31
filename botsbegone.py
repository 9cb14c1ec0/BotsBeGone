#!/usr/bin/python3
import os
import json
import ipaddress

data_path = '/var/lib/BotsBeGone'
os.system(f'/bin/git -C {os.path.join(data_path, "BotsBeGone")} pull origin')

with open(os.path.join(data_path, 'BotsBeGone', 'ip_addresses.json')) as new_file:
    new_data = json.load(new_file)

local_file_path = os.path.join(data_path, 'local', 'ip_addresses.json')
old_data = {}
if os.path.exists(local_file_path):
    with open(os.path.join(data_path, 'local', 'ip_addresses.json')) as old_file:
        old_data = json.load(old_file)
else:
    # this directory needs to exist to save data
    os.mkdir(os.path.join(data_path, 'local'))

new_addresses = []
removed_addresses = []

# new ip addresses
with open('/etc/ufw/user.rules') as ur:
    rules = ur.read()

head, separator, tail = rules.partition('### RULES ###')
finished_data = head + separator

for ip_address in new_data:
    if ip_address not in old_data:
        # roundtrip through the ipaddress library to prevent command injections in case of source repository compromise
        i = str(ipaddress.ip_address(ip_address))
        rule_proto = f'''\n\n### tuple ### deny any any 0.0.0.0/0 any {ip_address} in
-A ufw-user-input -s {i} -j DROP'''
        finished_data += rule_proto

finished_data += tail
with open('/etc/ufw/user.rules', 'w') as ur:
    ur.write(finished_data)
os.system('systemctl force-reload ufw.service')

# ip addresses to delete
for ip_address in old_data:
    if ip_address not in new_data:
        i = str(ipaddress.ip_address(ip_address))
        os.system(f'ufw delete deny from {i}')

# save new_data as old
with open(os.path.join(data_path, 'local', 'ip_addresses.json'), 'w') as local_file:
    json.dump(new_data, local_file)
