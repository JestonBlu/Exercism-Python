import nmap
import time

nm = nmap.PortScanner()
nm.scan('192.168.0.11-31')
hosts = nm.all_hosts()

while True:

    print("========================")

    for i in hosts:
        print("")
        print("IP    :", i)
        print("Host  :", nm[i].hostname())
        print("State :", nm[i].state())

    print("========================")

    time.sleep(10)
