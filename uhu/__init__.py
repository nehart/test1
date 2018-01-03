#!/usr/bin/python
# -*- coding: utf-8 -*-

import getpass
import sys
import telnetlib
import socket
import time
import re




###################################################################
# MAIN
###################################################################

def main():
    
    print("Hallo\n")
    user = input("Username: ")
    password = getpass.getpass(prompt='geheim: ', stream=None)
    
    print(user + "   " + password + "\n")

###################################################################
# start
###################################################################

if __name__ == "__main__":
    main()