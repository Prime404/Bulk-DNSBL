# Bulk-DNSBL
Quick and basic Python 3 script to lookup DNSBl for multiple IP-addresses from a list.

Example usage:
```
$ dnsbl_check.py -i example_servers.txt
<DNSBLResult: 114.115.149.234 [BLACKLISTED] (3/61)>
cbl.abuseat.org
dnsbl-1.uceprotect.net
rbl.interserver.net
<DNSBLResult: 8.8.8.8 was not found on any blacklist>
<DNSBLResult: 8.8.4.4 was not found on any blacklist>
```
