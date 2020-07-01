# Reverse CIDR Lookup

Perform a reverse CIDR lookup. That is, provide a CIDR range, and this
command will determine which IPs from the lookup belong to that range, 
and what services run on those IPs.

## ips.csv format
```
ip,service
10.0.0.1,"web"
10.0.0.2,"web"
10.0.0.3,"web"
10.0.0.4,"web"
10.0.1.1,"auth"
10.1.0.1,"db"
10.1.0.2,"db"
10.0.1.3,"db"
```


## Testing
```
cat test_in | ./reverse_cidr_lookup.py > test
diff test_out test
```
