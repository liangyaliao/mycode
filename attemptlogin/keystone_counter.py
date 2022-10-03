#!/usr/bin/env python3


def main():
    failed_login=0
    with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as logfile:
        for line in logfile:
            if "- - - - -] Authorization failed" in logfile:
                failed_login +=1
    print("failed times: " , failed_login)









main()
