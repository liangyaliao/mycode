#!/usr/bin/env python3

import os
import zipfile

def zipdir(dirpath,zipfileobj):
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            zipfileobj.write(os.path.join(root,file))
    #return None

def main():
    dirpath=input("which directory?")

    if os.path.isdir(dirpath):
        zippedfn = input("create a name for the zip: ")

        with zipfile.ZipFile(zippedfn,"w", zipfile.ZIP_DEFLATED) as zipfileobj:
            zipdir(dirpath,zipfileobj)

    else:
        print("not a valid dir")

main()        
