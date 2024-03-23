#!/usr/bin/env python

import subprocess

interface = "eth0"
new_mac = "00:11:22:33:44:66"

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True) # Can change the MAC address of eth0 to the given MAC address!
subprocess.call("ifconfig " + interface + " up", shell=True)