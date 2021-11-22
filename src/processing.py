# Process the gathered data from gather_users
import time
from gather_information import gather_information

def processing():
    info = gather_information()
    currentTime = int(time.time())
    return [active_peers(info,currentTime),peer_tx(info),peer_rx(info)]

# Currently Online Users (Handshake within the last 3 mins)
def active_peers(info,currentTime):
    online_peers = []
    for i in info:
        online_count = 0
        for j in info[i]:
            if (currentTime - int(j[5])) < 180: # This also takes care of the fact that users that have never came online will have timestamp of 0
                online_count +=1
        online_peers.append((i,online_count))
    return online_peers

def peer_tx(info):
    peer_tx_info = []
    for i in info:
        for j in info[i]:
            peer_tx_info.append((j[0],j[1],j[6]))
    return peer_tx_info

def peer_rx(info):
    peer_rx_info = []
    for i in info:
        for j in info[i]:
            peer_rx_info.append((j[0],j[1],j[7]))
    return peer_rx_info