#!/usr/bin/env python3
#open file in read mode
dnsfile = open("dnsservers.txt", "r")

#create list of lines
dnslist = dnsfile.readlines()

#loop over lines

for svr in dnslist:
    #print and end without a newline
    print(svr, end="\n")
    #close your file
    dnsfile.close()


dnsfile = open("dnsservers.txt", "r")
dnslist = dnsfile.readlines()

for svr in dnslist:
    print(svr)
    dnsfile.close()
