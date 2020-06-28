#!/bin/bash

#head /dev/urandom | tr -dc A-Za-z0-9 | head -c 13 ; echo ''
now=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 13 ; echo '')
echo "$now"

#smbpasswd -r 10.10.10.193 -U tlavel; ldapdomaindump -u fabricorp.local\\tlavel -p "$now" 10.10.10.193
smbpasswd -r 10.10.10.193 -U tlavel; rpcclient 10.10.10.193 -U tlavel -p "$now"
