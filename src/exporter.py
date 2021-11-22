# Nothing of value yet!
from prometheus_client import start_http_server, Gauge, Counter, Summary
import time
from processing import processing
scrape_timer = 1

# Create a metric to track current peer count per interface.
g_peercount = Gauge('wg_active_peer_total','Users that have their last handshake value less than 3 minutes',
                ['wginterface'])
g_peertx = Gauge('wg_peer_tx_bytes', 'Total Peer TX', ['wginterface', 'peer'])
g_peerrx = Gauge('wg_peer_rx_bytes', 'Total Peer RX', ['wginterface', 'peer'])

def set_peer_count():
    gathers = processing()
    for i in gathers[0]:
        g_peercount.labels(wginterface=f'{str(i[0])}').set(int(i[1]))

def set_peer_tx():
    gathers = processing()
    for i in gathers[1]:
        g_peertx.labels(wginterface=f'{str(i[0])}',peer=f'{str(i[1])}').set(int(i[2]))

def set_peer_rx():
    gathers = processing()
    print(gathers[2])
    for i in gathers[2]:
        g_peerrx.labels(wginterface=f'{str(i[0])}',peer=f'{str(i[1])}').set(int(i[2]))


REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')




# Get count of online users



# Main Loop
if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8989,'/metrics')
    # Generate some requests.
    while True:
        set_peer_count()
        set_peer_rx()
        set_peer_tx()
        time.sleep(scrape_timer)