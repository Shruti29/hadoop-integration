# The script examples provided by Cisco for your use are provided for reference only as a customer courtesay.  
# They are intended to facilitate development of your own scripts and software that interoperate with Cisco switches 
# and software.  Although Cisco has made efforts to create script examples that will be effective as aids to script 
# or software development,  Cisco assumes no liability for or support obligations related to the use of the script 
# examples or any results obtained using or referring to the script examples.

#
# Contact: sakommu@cisco.com
#
#
import socket
from cisco import *

HOST = '172.25.187.60'    # The remote host
PORT = 34567              # The same port as used by the server
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

#                print PORT.split()[7].replace("Eth1/","") + " " + serverName
                serverList[int(PORT.split()[7].replace("Eth1/",""))-1] = serverName
                break
print "======================================="
print "Port\tServer FQDN"
print "---------------------------------------"
for INDEX in range(48):
    if ( serverList[INDEX] ):
        print "Eth1/" + repr(INDEX+1) + "\t" + serverList[INDEX]  
print "======================================="
