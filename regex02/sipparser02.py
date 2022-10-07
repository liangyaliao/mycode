#!/usr/bin/env python3

import re

def main():

    with open('networktrace.txt') as trace:
        for line in trace:
            conobj = re.search(r'sip:\+(\d+)@\[(.*)\]:?(\d+)?', line)

            if conobj:
                print(conobj.group())
                print("the phone number is...")
                print(conobj.group(1))
                print("the IPv6 is...")
                print("conobj.group(2)")
                print("the port is...")
                print(conobj.group(3))
if __name__ == "__main__":
    main()

