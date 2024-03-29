#!/usr/bin/env python3
import crayons


def commandpush(devicecmd):
    for ip in devicecmd.keys():
        print(f"handshaking.... connecting with {ip}")
        for mycmds in devicecmd[ip]:
            print(f'Attempting to send commd--> {mycmds}')
    return None

def main():

    devicecmd={"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}


    print("Welcome to the network device command pusher")

    print("\nData set found\n")

    commandpush(devicecmd)

main()    
