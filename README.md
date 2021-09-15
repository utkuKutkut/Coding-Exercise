# Exercise-1
For the first exercise, I have used 192.168.252.0 as a network ID and 192.168.255.255 as a broadcast IP. You can find a detailed explanation in the document:https://github.com/utkuKutkut/Coding-Exercise/blob/main/Exercise-1/Generator.pdf \
Generate.sh file simply executes my python script with 1 command line argument which is the DATAPATH. All the server files will be written in this directory. In addition, I have named all files with their IP addresses. Each server generates its own LOG and writes the CPU usage of it's for 24 hours inside the file:
\
\
![alt text](https://github.com/utkuKutkut/Coding-Exercise/blob/main/Screenshot%20from%202021-09-14%2019-48-52.png)
\
\
Generating all LOG files took about 30 second for my computer. The content of each LOG file is like that:
\
\
![alt text](https://github.com/utkuKutkut/Coding-Exercise/blob/main/Screenshot%20from%202021-09-14%2019-50-05.png)


### query.sh file simply executes a python scripts with a command line argument, which is the path of our LOG files. (for me it's the same file)
\
\
![alt text](https://github.com/utkuKutkut/Coding-Exercise/blob/main/Screenshot%20from%202021-09-14%2019-51-11.png)


### And I can execute any query like that easily:
\
\
![alt text](https://github.com/utkuKutkut/Coding-Exercise/blob/main/Screenshot%20from%202021-09-14%2019-52-22.png)


### Even big queries (10 hours range) executes in milliseconds...
\
![alt text](https://github.com/utkuKutkut/Coding-Exercise/blob/main/Screenshot%20from%202021-09-14%2019-52-57.png)
\
\
![alt text](https://github.com/utkuKutkut/Coding-Exercise/blob/main/Screenshot%20from%202021-09-14%2019-53-22.png)


# Exercise-2
For the second exercise, I used JAVA since dealing with threads is more consistent. I ask the user to enter a number of threads for the producer and also for the consumer.\
Every time I create a thread, I call producer and consumer functions to execute. If my buffer (arrayList) is full capacity, the producer has to wait while the consumer removes the FIRST (oldest) element in the buffer. As soon as buffer capacity reliefs, the consumer thread takes the lock and produces new data, and puts it into the buffer. There will never be a deadlock since I use synchronized blocks for both threads. Here are the outputs of my sample case:\
\
\
![alt text](https://github.com/utkuKutkut/Coding-Exercise/blob/main/sc1.png)
\
\
\
\
![alt text](https://github.com/utkuKutkut/Coding-Exercise/blob/main/sc2.png)






