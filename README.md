# UDP_HEARTBEAT
# ✨Instruction
Build an UDP Heartbeat application. The Heartbeat can be
used to check if an application is up and running and to report one-way packet loss. The client
sends a sequence number and current timestamp in the UDP packet to the server, which is
listening for the Heartbeat (i.e., the UDP packets) of the client. Upon receiving the packets, the
server calculates the time difference and reports any lost packets. If the Heartbeat packets are
missing for some specified period of time, we can assume that the client application has stopped.
Implement the UDP Heartbeat (both client and server). You will need to modify the given
UDPPingerServer.py, and your UDP ping client.

# 🚀Implementation
## UDP HeartBeat client
The client should do the following:
1. sends the heartbeats with a sequence number and timestamp<br>
2. keeps sending packets at reqular intervals<br>
3. Does not expect a response.<br>

## UDP HeartBeat server
The server performs the following:
1. Listens for UDP packets.<br>
2. Tracks the last received sequence number and timestamp.<br>
3. Detects the lost packets by checking sequence gaps
4. Detects client failure, if no packet is received within a timeout period.

There's a 30% packet loss simulated by the client.



![Image](https://github.com/user-attachments/assets/2e0a2fda-aca8-40fe-96a4-c5296b73a0d7)

cc: Computer Networking: A Top Down Approach: Programming Assignments/UDP Pinger.
