import subprocess

online=[]
offline=[]

with open("iplist.txt","r") as file:
    ip_addresses=file.read().split("\n")


for ip in ip_addresses:
    send_ping = subprocess.call('ping %s -n 4' % ip)

    if (send_ping) == 0:
        online.append(ip)

    else:
        offline.append(ip)  

with open("reach.txt","w") as file:
    for x in online:
        file.write(x +"\n")

with open("not reach.txt","w") as file:
    for y in offline:
        file.write(y+"\n")
                          





