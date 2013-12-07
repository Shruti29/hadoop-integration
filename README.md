Hadoop Network Integration
==========================

Running the scripts
--------------------

Python Version 2.7 is needed to run these scripts.

There are two components to these scripts.  Server side and the switch side.  Server side component (appInfo.py) needs to be executed on any linux based server which has access to the hadoop cluster nodes that are connected to the concerned switch.

To run the script on the server:

<pre>python appInfo.py &</pre> 

The appInfo.py script is designed to run infinitely and provide any server related information requested by the Cisco Nexus Switch.  The scripts under the Nexus3548 are supposed to be run on the Nexus 3548.  They connect to the server component(appInfo.py) to gather the application related information.

For example, to run bufferServerMap.py, use:

<pre>python bufferServerMap.py</pre>


Brief description of scripts
-----------------------------

<h3>Server Side</h3>
--------------------

<h4>appInfo.py</h4>


This python script is for a server which is able to listen in on a port (56789), establish a TCP connection when a client (switch) attempts to 
make a connection, recieve data from the client and also request data from the client, and then repeat the process in an infinite loop. 

If the client sends a value of '1' to the server, the server willrequest the list of active trackers from the switch (client) side. 
If the the client sends a value of '2' to the server, the server will request list of active jobs from the swtich. 
If the client sends a value of '101', then the server will request a list of the MAC addresses of all devices connected to the switch. 


<h3>Switch side</h3>
--------------------

<h4>portServerMap.py</h4> 

This script also uses a connection to a remote server (port: 34567) to retrieve the fully qualified domain name of each server 
connected to the switch. The port and FQDN of each server is formatted in a table in the output.


Following is the example output of portServerMap.py script:
<pre>
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
</pre>


<h4>trackerList.py</h4> 

This script also establishes a connection to a remote server (port: 34567) and uses it to list out all servers connected to the 
switch which have trackers running on them. The output of the script will identify each server's name, its physical port on the switch 
side, and the listening port on the server side.  

Following is the example output of trackerList.py script:
<pre>
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
</pre>

<h4>bufferServerMap.py</h4>

This script operates on a particular switch, it establishes a connection with a remote server on the port 34567, uses it to 
retrieve the names of all the servers connected to the switch, and then lists out the buffer usage corresponding to each server at 
specific time intervals. 

Following is the example output of bufferServerMap.py script:
<pre>
n3548-001# bufferServerMap 
===================================================================
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
</pre>

Following is the example output of bufferServerMap.py script on 3064:
<pre>
n3064-001# bufferServerMap
====================================================================================================================
Port    Server          Q1      Q2      Q3      Q4      Q5      Q6      Q7      Q8      Q9      Q10     Q11     Q12
--------------------------------------------------------------------------------------------------------------------
Eth1/1  c240-m3-008     3       0       0       0       0       0       0       0       0       0       0       0       
Eth1/2  c240-m3-001     117     0       0       0       0       0       0       0       0       0       0       0       
Eth1/3  c240-m3-004     0       0       0       0       0       0       0       0       0       0       0       0       
Eth1/4  c240-m3-002     0       0       0       0       0       0       0       0       0       0       0       0       
Eth1/5  c240-m3-007     0       0       0       0       0       0       0       0       0       0       0       0       
Eth1/6  c240-m3-005     0       0       0       0       0       0       0       0       0       0       0       0       
Eth1/7  c240-m3-003     0       0       0       0       0       0       0       0       0       0       0       0       
Eth1/8  c240-m3-009     4       0       0       0       0       0       0       0       0       0       0       0       
.
.
.
</pre>


<h4>jobsBuffer.py</h4>

This script will include the functionality of the bufferServerMap.py script, and it will also provide more details (running 
time, priority, user) on the jobs that were running during peak buffer usage. 

Following is the example output of jobsBuffer.py script:
<pre>
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
.
</pre>

Following is the example output of jobsBuffer.py script on 3064:
<pre>
python bootflash:jobsBuffer.py
Hadoop Job Info ... 
===================================================================
1 jobs currently running
JobId           RunTime(secs)   User    Priority
job_201310292020_0005   32      hadoop  NORMAL  
===================================================================
====================================================================================================================
Port    Server          Q1      Q2      Q3      Q4      Q5      Q6      Q7      Q8      Q9      Q10     Q11     Q12
--------------------------------------------------------------------------------------------------------------------
Eth1/1  c240-m3-008     3       0       0       0       0       0       0       0       0       0       0       0       
Eth1/2  c240-m3-001     0       0       0       0       0       0       0       0       0       0       0       0       
Eth1/3  c240-m3-004     35      0       0       0       0       0       0       0       0       0       0       0       
Eth1/4  c240-m3-002     3       0       0       0       0       0       0       0       0       0       0       0       
Eth1/5  c240-m3-007     407     0       0       0       0       0       0       0       0       0       0       0       
Eth1/6  c240-m3-005     268     0       0       0       0       0       0       0       0       0       0       0       
Eth1/7  c240-m3-003     0       0       0       0       0       0       0       0       0       0       0       0       
Eth1/8  c240-m3-009     0       0       0       0       0       0       0       0       0       0       0       0       
.
.
.
</pre>
