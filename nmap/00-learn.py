import nmap

nm = nmap.PortScanner()

nm.scan('192.168.0.11-31')

hosts = nm.all_hosts()

# a more usefull example :
for i in hosts:
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (i, nm[i].hostname()))
    print('State : %s' % nm[i].state())


nm.scan(hosts='192.168.0.1/24', arguments='-n -sP -PE -PA21,23,80,3389')
