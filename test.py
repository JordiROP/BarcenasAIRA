#!/usr/bin/python

import os

if __name__ == '__main__' :

    print "++++++++++++++++++++++++++++++++++++++++"
    print "+++++++++++++++++TEST1++++++++++++++++++"
    print "++++++++++++++++++++++++++++++++++++++++"

    cmd = "./findingBarcenas.py 3 [1,1,0,-1,0],[1,2,1,0,-1],[1,3,0,-1,-1]" \
            ",[2,3,1,-1,-1],[3,3,0,-1,-1]"
    os.system(cmd)

    print "Expected result Test1:"
    print "0 0 0"
    print "0 1 0"
    print "0 0 0"


    print "++++++++++++++++++++++++++++++++++++++++"
    print "+++++++++++++++++TEST2++++++++++++++++++"
    print "++++++++++++++++++++++++++++++++++++++++"

    cmd = "./findingBarcenas.py 4 [1,1,0,-1,1],[1,2,0,0,-1]"
    os.system(cmd)

    print "Expected result Test2:"
    print "1 0 0 0"
    print "1 0 0 0"
    print "0 0 0 0"
    print "0 0 0 0"

    print "++++++++++++++++++++++++++++++++++++++++"
    print "+++++++++++++++++TEST3++++++++++++++++++"
    print "++++++++++++++++++++++++++++++++++++++++"

    cmd = "./findingBarcenas.py 5 [1,1,0,-1,-1],[2,1,0,-1,-1],[2,2,0,-1,0],"\
            "[2,3,0,0,-1]"
    os.system(cmd)

    print "Expected result Test3:"
    print "0 0 1 1 1"
    print "0 0 1 1 1"
    print "0 0 0 1 1"
    print "0 0 0 0 1"
    print "0 0 0 1 1"

    print "++++++++++++++++++++++++++++++++++++++++"
    print "+++++++++++++++++TEST4++++++++++++++++++"
    print "++++++++++++++++++++++++++++++++++++++++"

    cmd = "./findingBarcenas.py 6 [1,1,1,-1,-1],[2,1,1,-1,-1],[2,2,0,-1,0],"\
            "[2,3,0,1,-1],[3,3,1,-1,-1]"
    os.system(cmd)

    print "Expected result Test4:"
    print "0 0 0 0 0 0"
    print "0 0 0 0 0 0"
    print "0 0 0 0 0 0"
    print "0 0 0 0 0 0"
    print "0 0 0 0 0 0"
    print "0 0 0 0 0 0"
