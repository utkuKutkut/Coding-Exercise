import os
import sys
import time
import datetime
import random
from datetime import datetime, date, timedelta

dataPath = sys.argv[1]
print("Generating... Please wait.")


''' about the IP address: we need 1000 servers to host. '''
'''MASK: 22 = 2^10 ip addresses = 1024... '''
'''Let's say our network ID: 192.168.252.0 /22 then broadcast would be: 192.168.255.255 /22'''
'''We only need 1000 hosts: 192.168.252.1 - 192.168.255.255'''

#sample date. We need to track the CPU usage of every minute in a day ...
s = "2014-10-31 00:00:00"

'''we have 1440 minutes in a day. It will be costly since we have 1000 servers that generate logs in every minute (1440*1000*2)'''
for mins in range(0, 1440):
    s = datetime.strptime(str(s), '%Y-%m-%d %H:%M:%S')
    s = time.mktime(datetime.strptime(str(s), "%Y-%m-%d %H:%M:%S").timetuple())
    count = 0
    for i in range(252, 256):
        for j in range(0, 256):
            if(count == 1000): break
            if(i == 252 and j == 0): continue #since it's the network ID, we cannot assign that IP to a host#
            if(i == 255 and j == 255): continue  #notice it's not actually needed since we stop looping when we reached 1000 IPs#
            ip = "192.168."+str(i)+"."+str(j)
            count+=1
            cpu1 = random.randrange(1, 100)
            cpu2 = random.randrange(1, 100)
            s = int(s)
            data1 = (str(s)+" "+ip+" 0 "+str(cpu1))
            data2 = (str(s)+" "+ip+" 1 "+str(cpu2))
            
            completeName = os.path.join(dataPath, ip)
            file1 = open(completeName, "a")
            file1.write(data1+" \n")
            file1.write(data2+" \n")
            file1.close()
    s = datetime.fromtimestamp(s)
    s = s + timedelta(minutes = 1)