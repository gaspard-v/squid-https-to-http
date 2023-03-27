# Squid HTTPS to HTTP

## Quick Launch

install nginx and change the default server with the content of `nginx_default_vhost.conf`.

install Squid and add the line `dns_nameservers 127.0.0.1` in your `squid.conf` file.

install Python3 and pip, launch `pip install -r requirements.txt` and launch the custom DNS server `python dns_localhost.py`

## Check

Check if eveything is working well: `curl --proxy 127.0.0.1:3128 www.google.com`, it should print the www.google.com's source code.
