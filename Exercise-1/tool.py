
import os
import sys
import time
import datetime
from datetime import datetime, date, timedelta
import os

dataPath = sys.argv[1]
while True:
    inp = input("\n>")
    if(inp == "EXIT" or inp == "exit"): break
    inp = inp.split(' ')
    filePath = inp[1]
    cpu = inp[2]

    completeName = os.path.join(dataPath, filePath)

    file1 = open(completeName, 'r')
    Lines = file1.readlines()


    startDate = inp[3]
    startDate += " "+inp[4]

    exSDate = inp[5]
    exSDate += " "+inp[6]

    s = datetime.strptime(exSDate, '%Y-%m-%d %H:%M')
    s = time.mktime(datetime.strptime(str(s), "%Y-%m-%d %H:%M:%S").timetuple())
    s = int(s)
    s2 = datetime.strptime(startDate, '%Y-%m-%d %H:%M')
    s2 = time.mktime(datetime.strptime(str(s2), "%Y-%m-%d %H:%M:%S").timetuple())
    s2 = int(s2)



    print("\nCPU"+cpu+ " usage on "+filePath+":\n")
    for i in Lines:
        timeStamp = i.split(" ")[0]
        cpuID = i.split(" ")[2]
        if(int(timeStamp) >= int(s2) and cpuID == cpu):
            date = datetime.fromtimestamp(int(timeStamp))
            consume = i.split(" ")[3]
            print("("+str(date)+", "+consume+"%"+") ", end="")
            if(timeStamp == str(s)):
                break
    print("\n")
