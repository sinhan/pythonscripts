#!/usr/bin/env python3.3
import os
import sys

def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print os.path.abspath(full_path)
            #print(os.path.normpath(os.path.abspath(full_path)))
            print relpath


if __name__ == '__main__':
	findfile(sys.argv[1], sys.argv[2])
