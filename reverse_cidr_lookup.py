#!/usr/local/bin/python3

import csv, sys, ipaddress

# build table of ipaddress
ips = []
t = csv.DictReader(open("ips.csv"))
for l in t:
    ips.append([ipaddress.ip_address(l["ip"]),l["service"]])

# process entries
r = csv.reader(sys.stdin)
for l in r:
    out = ""
    try:
        out = l[1]
        cidr = ipaddress.ip_network(l[0])
        svcs = []
        for ip in ips:
            if ip[0] in cidr and ip[1] not in svcs:
                svcs.append(ip[1])
        if len(svcs)>0:
            svcs = sorted(svcs) # sort and dedupe
            out = ','.join(svcs)
    except:
        pass
    finally:
        print("\"{}\",\"{}\"".format(l[0],out))
