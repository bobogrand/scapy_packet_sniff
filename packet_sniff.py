from scapy.all import *
 
## Create a Packet Counter
counter = 0
 
## Define our Custom Action function
def custom_action(packet):
    global counter
    counter += 1

    packet.display()
    
    if packet.getlayer("Raw"):
         hexdump(packet.getlayer("Raw"))
 
## Setup sniff, filtering for IP traffic
sniff(filter="ip", prn=custom_action,store=0)
