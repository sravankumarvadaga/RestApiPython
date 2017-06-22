#!/usr/bin/python
import sys

def move(args):
    name = args[0]
    if name == 'forward':
        print ('moving forward')
    else:
        print ('sorry mate, I cant move')

if __name__== "__main__":
    move(sys.argv[1:])