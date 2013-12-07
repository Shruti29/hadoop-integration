# The script examples provided by Cisco for your use are provided for reference only as a customer courtesay.  
# They are intended to facilitate development of your own scripts and software that interoperate with Cisco switches 
# and software.  Although Cisco has made efforts to create script examples that will be effective as aids to script 
# or software development,  Cisco assumes no liability for or support obligations related to the use of the script 
# examples or any results obtained using or referring to the script examples.

# Nexus 3548

import socket
from cisco import *

HOST = '172.25.187.60'
PORT = 34567
appSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
appSocket.connect((HOST, PORT))
appSocket.sendall("101")
appData = appSocket.recv(10240)
appSocket.close()

serverList = []
for INDEX in range(48):
    serverList.append("")

macTable=CLI("show mac address-table dynamic | grep Eth", False)
for PORT in macTable.get_output():
    if ( len(PORT) > 0 ):
        MAC=PORT.split()[2].replace('.','')

        for serverMAC in appData.split():

            if ( MAC in serverMAC ):
                serverName = serverMAC.split(',')[0]

                serverList[int(PORT.split()[7].replace("Eth1/",""))-1] = serverName
                break

appSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
appSocket.connect((HOST, PORT))
appSocket.sendall("2")
appData = appSocket.recv(10240)
appSocket.close()

bufferUsageList = []

for INDEX in range(48):
    serverList.append("")
    bufferUsageList.append("")

bufferTable=CLI("show hardware profile buffer monitor brief | grep Ethernet", False)
for PORT in bufferTable.get_output():
    if ( len(PORT) > 0 ):
        portNo = PORT.split()[0].split("/")[1]
        bufferUsage = ""
        for INDEX in [1,2,3,4,5]:
            bufferUsage = bufferUsage + PORT.split()[INDEX] + "\t"

        bufferUsageList[int(portNo)-1] = bufferUsage

print "Hadoop Job Info ... "
print "==================================================================="
print appData.split("\n")[0]
print "JobId\t\tRunTime(secs)\tUser\tPriority"
jobData = ""
for data in appData.split("\n"):
    if ( "job_" in data ):
        for value in data.split(","):
            jobData = jobData + value + "\t"
        jobData = jobData + "\n"
print jobData
print "==================================================================="

print "Buffer Info - Per Port"
print "Port\tServer\t\t\t1sec\t5sec\t60sec\t5min\t1hr"
print "-------------------------------------------------------------------"
for INDEX in range(48):
    if ( serverList[INDEX] ):
        print "Eth1/" + repr(INDEX+1) + "\t" + serverList[INDEX].split(".")[0] + "\t" + bufferUsageList[INDEX] 
print "==================================================================="

