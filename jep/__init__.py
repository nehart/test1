#
# Test
#
# written by Norbert EHART
# import wasweiß denn ich!
#
#

import getpass
import sys
import telnetlib
import socket
import time
import re

from jep.mod01 import *




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
