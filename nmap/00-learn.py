#! python
import nmap

nm = nmap.PortScanner()

nm.scan('192.168.0.11-20')

hosts = nm.all_hosts()

for i in hosts:
    nm[i].state()
