hadoop-integration
==================


BRIEF DESCRIPTION OF SCRIPTS:
-----------------------------


SERVER SIDE 
-----------

appinfo.py
----------

This python script is for a server which is able to listen in on a port (56789), establish a TCP connection when a client (switch) attempts to 
make a connection, recieve data from the client and also request data from the client, and then repeat the process in an infinite loop. 

If the client sends a value of '1' to the server, the server willrequest the list of active trackers from the switch (client) side. 
If the the client sends a value of '2' to the server, the server will request list of active jobs from the swtich. 
If the client sends a value of '101', then the server will request a list of the MAC addresses of all devices connected to the switch. 


SWITCH SIDE (NEXUS 3548)
------------------------

bufferServerMap.py 
------------------

This script operates on a particular switch, it establishes a connection with a remote server on the port 34567, uses it to 
retrieve the names of all the servers connected to the switch, and then lists out the buffer usage corresponding to each server at 
specific time intervals. 

jobsBuffer.py 
-------------

This script will include the functionality of the bufferServerMap.py script, and it will also provide more details (running 
time, priority, user) on the jobs that were running during peak buffer usage. 

portServerMap.py 
----------------

This script also uses a connection to a remote server (port: 34567) to retrieve the fully qualified domain name of each server 
connected to the switch. The port and FQDN of each server is formatted in a table in the output.

trackerList.py 
--------------

This script also establishes a connection to a remote server (port: 34567) and uses it to list out all servers connected to the 
switch which have trackers running on them. The output of the script will identify each server's name, its physical port on the switch 
side, and the listening port on the server side.  


-----------------------------------------------------------------------------------------------------------------------------------


RUNNING THE SCRIPTS:
--------------------

 
PYTHON VERSION 2.7 is needed to run these scripts
-------------------------------------------------


In order to run these scripts, the user must first log into a remote server and run the appinfo.py script:

python appinfo.py 

The appinfo.py script will run for an infinite amount of time on the server side, and so now, any of the switch side script can be 
made to run on a nexus 3548 series switch which has python enabled.

For example, to run bufferServerMap.py, use:

python bufferServerMap.py


-------------------------------------------------------------------------------------------------------------------------------------

EXAMPLE OUTPUTS FOR SCRIPTS ON SERVER SIDE:
-------------------------------------------


bufferServerMap.py 
------------------


n3548-001# bufferServerMap ===================================================================
Port    Server                  1sec    5sec    60sec   5min    1hr
-------------------------------------------------------------------
Eth1/1  c200-m2-10g2-001        0KB     0KB     0KB     0KB     0KB     
Eth1/2  c200-m2-10g2-002        384KB   384KB   1536KB  2304KB  2304KB  
Eth1/3  c200-m2-10g2-003        384KB   384KB   1152KB  1536KB  1536KB  
Eth1/4  c200-m2-10g2-004        384KB   384KB   2304KB  2304KB  2304KB  
Eth1/5  c200-m2-10g2-005        384KB   384KB   768KB   1536KB  1536KB  
Eth1/6  c200-m2-10g2-006        384KB   2304KB  2304KB  2304KB  2304KB  
Eth1/7  c200-m2-10g2-031        384KB   384KB   3456KB  3840KB  3840KB  
Eth1/8  c200-m2-10g2-008        768KB   768KB   2688KB  2688KB  2688KB  
Eth1/9  c200-m2-10g2-009        384KB   384KB   2304KB  2304KB  2304KB 
Eth1/11 c200-m2-10g2-011        384KB   384KB   1920KB  1920KB  1920KB   
.
.
.



jobsBuffer.py 
-------------


n3548-001# jobsBuffer
Hadoop Job Info ... 
===================================================================
1 jobs currently running
JobId           RunTime(secs)   User    Priority
job_201306131423_0009   120     hadoop  NORMAL  
===================================================================
Buffer Info - Per Port
Port    Server                  1sec    5sec    60sec   5min    1hr
-------------------------------------------------------------------
Eth1/1  c200-m2-10g2-001        0KB     0KB     0KB     0KB     0KB     
Eth1/2  c200-m2-10g2-002        384KB   384KB   768KB   768KB   768KB   
Eth1/3  c200-m2-10g2-003        384KB   384KB   1152KB  1152KB  1152KB  
Eth1/4  c200-m2-10g2-004        384KB   1536KB  1536KB  1536KB  1536KB  
Eth1/5  c200-m2-10g2-005        384KB   768KB   1152KB  1152KB  1152KB  
.
.



portServerMap.py 
----------------


n3548-001# portServerMap
=======================================
Port    Server FQDN
---------------------------------------
Eth1/1  c200-m2-10g2-001.cluster10g.com
Eth1/2  c200-m2-10g2-002.cluster10g.com
Eth1/3  c200-m2-10g2-003.cluster10g.com
Eth1/4  c200-m2-10g2-004.cluster10g.com
Eth1/5  c200-m2-10g2-005.cluster10g.com
Eth1/6  c200-m2-10g2-006.cluster10g.com
Eth1/7  c200-m2-10g2-031.cluster10g.com
Eth1/8  c200-m2-10g2-008.cluster10g.com
Eth1/9  c200-m2-10g2-009.cluster10g.com
Eth1/11 c200-m2-10g2-011.cluster10g.com
.
.
.



trackerList.py 
--------------


n3548-001# trackerList
===========================================
Port    Server                  Server Port
-------------------------------------------
Eth1/2  c200-m2-10g2-002        50544
Eth1/3  c200-m2-10g2-003        41909
Eth1/4  c200-m2-10g2-004        36480
Eth1/5  c200-m2-10g2-005        38179
Eth1/6  c200-m2-10g2-006        51375
Eth1/7  c200-m2-10g2-031        41915
Eth1/8  c200-m2-10g2-008        50983
Eth1/9  c200-m2-10g2-009        37056
Eth1/11 c200-m2-10g2-011        35882
Eth1/12 c200-m2-10g2-012        44551
.
.
.

