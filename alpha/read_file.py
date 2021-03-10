#!/usr/bin/python

import sys

def main(files):
    for f in files:
        # To debug
        print "Esssa ", f

        f = open('files/' +f, "r")
        print(f.read())

if __name__ == "__main__":
    files = sys.argv[1:]
    main(files)