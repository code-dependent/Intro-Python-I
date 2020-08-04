"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys

def sysargs():
    for arg in sys.argv :
        print(arg)

def sysos():
    print(sys.platform)

sysos()

def sysv():
    print(sys.version)
sysv()

def osid():
    print(os.geteuid())


osid()
"""# Print the current working directory (cwd):
# YOUR CODE HERE"""
def oscwd():
    print(os.getcwd())


oscwd()

"""# Print out your machine's login name
# YOUR CODE HERE"""