#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
#print(configfile.read())

## close file
configfile.close()

configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
#print(configlist)

for x in configlist:
    #print(x)

    print(x.splitlines())
configfile.close()    
