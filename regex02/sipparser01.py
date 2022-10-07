#!/usr/bin/env python3

import re

def main():
    contact = "Contact: <sip:+17175664428@[2600:2304:9210:ec::2]:5060;eri-generated-at=10.172.0.132>"

    conobj = re.search(r'sip:\+(\d+)@\[(.*)\]:?(\d+)?', contact)

    if conobj:
        print(conobj.group())

        print("the phone number is ...")
        print(conobj.group(1))

        print("the IPv6 is...")
        print(conobj.group(2))

        print("the port is...")
        print(conobj.group(3))
main()
