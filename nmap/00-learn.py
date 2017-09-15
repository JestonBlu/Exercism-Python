import nmap
import time

nm = nmap.PortScanner()
nm.scan('192.168.0.11-31')
hosts = nm.all_hosts()

while True:
    file = open("test.txt", "w")

    file.write("========================\n")

    for i in hosts:
        file.write("\n")
        file.write("IP    :" + i + "\n")
        file.write("Host  :" + nm[i].hostname() + "\n")
        file.write("State :" + nm[i].state() + "\n")

    file.write("========================")

    file.close()
    time.sleep(10)
