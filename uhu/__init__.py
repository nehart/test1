#!/usr/bin/python
# -*- coding: utf-8 -*-

import getpass
import sys
import telnetlib
import socket
import time
import re

from uhu.mod01 import *




###################################################################
# MAIN
###################################################################

def main():
    
    print("Hallo\n")
    hallo()
    user = input("Username: ")
    password = getpass.getpass(prompt='geheim: ', stream=None)
    
    print(user + "   " + password)

###################################################################
# start
###################################################################

if __name__ == "__main__":
    main()