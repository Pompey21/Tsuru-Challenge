import sys
from packet import Packet
from file_header import Header


"""
    HELPER METHODS (called throughout this file)
"""
def get_PCAP_header(data):
    pcap_header = data[:48]
    return pcap_header, data[48:]

def generate_packets(data):
    packets = []
    counter = 0
    # while (counter<8):
    while (len(data) != 0):
        packet,data = packet_formation(data)
        # filtering the packets that do not contain B6034 in the body!
        if packet.flag:
            packets.append(packet)
        counter += 1
    return packets

def packet_formation(data):
    packet = Packet(data)
    data = data[packet.total_size:]
    return packet, data

def write_text_file(packets):
    with open('packets_info.txt','w') as file:
        for packet in packets:
            file.write(str(packet.package_time) + ' ' + str(packet.accept_time) + ' '
                       + str(packet.issue_code) + ' ' + str(packet.bids.first_bid[0])
                       + '@' + str(packet.bids.first_bid[1]) + ' '
                       + str(packet.bids.second_bid[0]) + '@' + str(packet.bids.second_bid[1]) + ' '
                       + str(packet.bids.third_bid[0]) + '@' + str(packet.bids.third_bid[1]) + ' '
                       + str(packet.bids.fourth_bid[0]) + '@' + str(packet.bids.fourth_bid[1]) + ' '
                       + str(packet.bids.fifth_bid[0]) + '@' + str(packet.bids.fifth_bid[1]) + ' '
                       + str(packet.asks.first_ask[0]) + '@' + str(packet.asks.first_ask[1]) + ' '
                       + str(packet.asks.second_ask[0]) + '@' + str(packet.asks.second_ask[1]) + ' '
                       + str(packet.asks.third_ask[0]) + '@' + str(packet.asks.third_ask[1]) + ' '
                       + str(packet.asks.fourth_ask[0]) + '@' + str(packet.asks.fourth_ask[1]) + ' '
                       + str(packet.asks.fifth_ask[0]) + '@' + str(packet.asks.fifth_ask[1]) + ' '
                       + '\n')

# =============================================================================
# The Script for analysing the .pcap file
# =============================================================================

"""
1.  First thing I need to do, is to read the PCAP file, and separate the header from
    the packet information.
"""
path = '/Users/admin/Desktop/Tsuru-Prep/Tsuru-Python/original_file.pcap'
with open(path, 'r') as file:
    data = file.read().replace('\n','').replace(' ','')

"""
2.  Second thing I need to do, is to check if the script was ran with the '-r'
    command, which means the packets should be arranged based on 'quote accept time'.
"""
try:
    if sys.argv[1] == '-r':
        flag = True
    else:
        flag = False
except:
    flag = False

"""
3.  Third thing I need to do, is to get the PCAP header information as well as every packet's
    information.
"""
pcap_header,data = get_PCAP_header(data)
header = Header(pcap_header)
packets = generate_packets(data)

"""
4.  Fourth thing I need to do, is to sort the packets if the '-r' command was ran.
"""
if flag:
    packets.sort(key=lambda packet: packet.accept_time)

"""
5.  Fifth thing I need to do, is to write the packet's information into a text file.
"""
write_text_file(packets)


print('Quod Erat Demonstrandum')





