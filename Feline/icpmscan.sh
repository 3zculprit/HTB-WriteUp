#!/bin/bash

for i in $(seq 1 255); do
 ping -W 1 -c 1 172.18.0.$i > /dev/null && echo "Host Alive : 172.18.0.$i" || echo "Host Dead: 172.18.0.$i"
done
