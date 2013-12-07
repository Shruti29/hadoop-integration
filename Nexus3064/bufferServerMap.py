# The script examples provided by Cisco for your use are provided for reference only as a customer courtesay.
# They are intended to facilitate development of your own scripts and software that interoperate with Cisco switches
# and software.  Although Cisco has made efforts to create script examples that will be effective as aids to script
# or software development,  Cisco assumes no liability for or support obligations related to the use of the script
# examples or any results obtained using or referring to the script examples.

# Nexus 3064

import re
import sys

from cisco import *

#print "Test starts at "+cli('show clock')[1]
import socket
from cisco import *

HOST = '172.25.187.107' # The remote host
PORT = 34567 # The same port as used by the server
appSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
appSocket.connect((HOST, PORT))

appSocket.sendall("101")
appData = appSocket.recv(10240)
appSocket.close()

serverList = []
bufferUsageList = []

for INDEX in range(0,65):
    serverList.append("")
    bufferUsageList.append("")

macTable=CLI("show mac address-table dynamic | grep Eth", False)
for PORT in macTable.get_output():
    if ( len(PORT) > 0 ):
        MAC=PORT.split()[2].replace('.','')

        for serverMAC in appData.split():

            if ( MAC in serverMAC ):
                serverName = serverMAC.split(',')[0]

# print PORT.split()[7].replace("Eth1/","") + " " + serverName
                serverList[int(PORT.split()[7].replace("Eth1/",""))] = serverName
                break

bufferTable = CLI('show hardware internal buffer info pkt-stats detail | beg "\["',False)
flag = 0
bufferUsage = ""

for PORT in bufferTable.get_output():
    if len(re.findall('\[',PORT)):
        portNo = PORT.split("[")[1]
        portNo = portNo.split("]")[0]
        flag = 1
        bufferUsage = ""
    if flag:
        if len(re.findall('UC',PORT)):
            for INDEX in [1,2,3,4,5,6,7,8]:
                bufferUsage = bufferUsage + PORT.split()[INDEX] + "\t"
        if len(re.findall('MC',PORT)):
            for INDEX in [1,2,3,4]:
                bufferUsage = bufferUsage + PORT.split()[INDEX] + "\t" 
            flag = 0
    if not flag:
        if bufferUsage:
            if (int(portNo) < 9):
                #print int(portNo)
                bufferUsageList[int(portNo)] = bufferUsage
                #print portNo+"=>"+bufferUsageList[int(portNo)]
                bufferUsage = "" 
print "===================================================================================================================="
print "Port\tServer\t\tQ1\tQ2\tQ3\tQ4\tQ5\tQ6\tQ7\tQ8\tQ9\tQ10\tQ11\tQ12"
print "--------------------------------------------------------------------------------------------------------------------"
for INDEX in range(1,65):
    if ( serverList[INDEX] ):
        print "Eth1/" + repr(INDEX) + "\t" + serverList[INDEX].split(".")[0] + "\t" + bufferUsageList[INDEX]
print "===================================================================================================================="
#print "Test ends at "+cli('show clock')[1]
