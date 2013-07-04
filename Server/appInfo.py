# The script examples provided by Cisco for your use are provided for reference only as a customer courtesay.  
# They are intended to facilitate development of your own scripts and software that interoperate with Cisco switches 
# and software.  Although Cisco has made efforts to create script examples that will be effective as aids to script 
# or software development,  Cisco assumes no liability for or support obligations related to the use of the script 
# examples or any results obtained using or referring to the script examples.


from socket import *
import commands

# Listener port #
PORT = 56789

# Socket setup
appServerSocket = socket(AF_INET, SOCK_STREAM)
appServerSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)#
appServerSocket.bind((HOST, PORT))
appServerSocket.listen(5)

# Stay in an infinite loop
# you could kill this loop by connecting to the server 
# on the above port via telnet and enter 0
while True:
    connection_failed = False
    try:
        conn, addr = appServerSocket.accept()
    except:
        connection_failed = True
        pass

    if ( connection_failed != True ):
        data = int(conn.recv(1024))

        if ( data == 0 ):
           break

# 3 options for this example script - could be expanded to integrate any info
# 1. list of active trackers,
# 2. list of jobs
# 3. MAC address's of all the nodes

        elif ( data == 1 ):
            appData = commands.getoutput("hadoop job -list-active-trackers")

        elif ( data == 2 ):
            jobList = commands.getoutput("hadoop job -list | grep -i Job")
            currentTime = commands.getoutput("date +%s")

            appData = jobList.split("\n")[0] + "\n"
            for eachJob in jobList.split("\n"):
                if ( "job_" in eachJob ):
                    appData = appData + eachJob.split()[0] + ","
                    appData = appData + repr(int(currentTime) - int(int(eachJob.split()[2])/1000)) + ","
                    appData = appData + eachJob.split()[3] + ","
                    appData = appData + eachJob.split()[4] + "\n"

        elif ( data == 101 ):
            appData = commands.getoutput("getMACs.sh")

        else:
            appData = "No Data!"

        conn.sendall(appData)
        conn.close()
