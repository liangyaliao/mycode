#!/usr/bin/env python3

import requests

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    
    groundctrl = requests.get(MAJORTOM)

    helmetson = groundctrl.json()

   #print("\n\nConverted Python data")
    #print(helmetson)
    
    print('\n\nPeople in spaces: ', helmetson['number'])
    people = helmetson['people']
    print(people)

main()    
