#system libraries
import subprocess
import random
import os
import random
import time
import sys

#Networking Libraries
from spoofmac.util import random_mac_address, MAC_ADDRESS_R, normalize_mac_address
from spoofmac.interface import (
    wireless_port_names,
    find_interfaces,
    find_interface,
    set_interface_mac,
    get_os_spoofer
)
import socket
import netifaces

def change_ip(interface_name,ip_address,mask,gateway):
    ip_address='.'.join(ip_address.split('.')[:-1])+'.'+ str(random.randrange(8,255-int(mask.split('.')[-1])-1))
    result_1=subprocess.call('netsh interface ipv4 set address name="%s" static %s %s %s'%(interface_name,ip_address,mask,gateway), shell=True)
    result_2=subprocess.call('netsh interface ipv4 set dns name="%s" static 8.8.8.8'%(interface_name), shell=True)
    if(result_1==1 or result_2==1):
        print("[WARN] Unable to change IP. Run the program with admin rights.")
        sys.exit()
        return False
    print("[INFO] New IP Address is: %s"%(ip_address))
    return True

def get_default_network_details():
    def get_ip_address():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address=s.getsockname()[0]
        s.close()
        return ip_address
    ip_address = get_ip_address()
    for i in netifaces.interfaces():
        try:
            if(str(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])==str(ip_address)):
                print("[INFO] *Default Network Details*")
                print("[INFO] IP Address: ", ip_address)
                print("[INFO] Mask: ", netifaces.ifaddresses(i)[netifaces.AF_INET][0]['netmask'])
                print("[INFO] Gateway: ", netifaces.gateways()['default'][netifaces.AF_INET][0])
                delay(5,5)
                return ip_address, netifaces.ifaddresses(i)[netifaces.AF_INET][0]['netmask'], netifaces.gateways()['default'][netifaces.AF_INET][0]
        except:
            print("no element found")
            pass

def changing_ip():
    #SETTINGS
    #Please check your network details 
    interface_name = "Intel(R) Wireless-N 7260" #netsh interface ipv4 show config
    ip_address,mask,gateway = get_default_network_details()
    try:
        print("[INFO] *Changing MAC & IP*")
        print("[INFO] New Mac is: "+random_mac_address(interface_name))
        delay(3,5)
        change_ip(interface_name,ip_address,mask,gateway)
        delay(3,5)
    except:
        print('error changing, quitting ..')
        pass