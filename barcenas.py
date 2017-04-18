#!/usr/bin/python

import sys, copy

def intersectLocInfo(f):
    f.write("intersectLocInfo( 0, _, 0 ).\n")
    f.write("intersectLocInfo( _, 0, 0 ).\n")
    f.write("intersectLocInfo( 1, Y, Y ).\n")
    f.write("intersectLocInfo( X, 1, X ).\n")

    f.write("intersectRow( [], [], [] ).\n\n")

    f.write("intersectRow( [PH|PT], [NH|NT], [FH|FT] ) :-\n")
    f.write("            intersectLocInfo( PH, NH, FH ),\n")
    f.write("            intersectRow( PT, NT, FT ).\n\n")

    f.write("intersectLocs( [], [], [] ).\n\n")

    f.write("intersectLocs( [PrevRow|PrevLocs], [NewRow|NewLocs]," +
                            "FinalLocs ) :-\n")
    f.write("             intersectRow( PrevRow, NewRow, FinalRow ),\n")
    f.write("             intersectLocs( PrevLocs, NewLocs, RestOfRows ),\n")
    f.write("             FinalLocs = [ FinalRow | RestOfRows ].\n\n")

def isBarcenasAround(f, size):
    possibleLocs = list()
    for x in xrange(size):
        for y in xrange(size):
            world = setPossibleLocs(x, y, size)
            possibleLocs.append(world)
            f.write("isBarcenasAround( "+ str(x+1) + ", " + str(y+1) +
                    ", 0, " + str(world) + " ).\n")
    f.write("\n\n")
    pos = 0
    for x in xrange(size):
        for y in xrange(size):
            reversedWorld = reverseWorld(possibleLocs[pos], size)
            f.write("isBarcenasAround( "+ str(x+1) + ", " + str(y+1) + ", 1, "
                    + str(reversedWorld) + " ).\n")
            pos += 1

    f.write("\n\n")

def rajoyAndCospedal(f, size):

    leftWorld = barcenasLeft(size)
    rightWorld = barcenasRight(size)

    for column in xrange(size):
        f.write("rajoyAndCospedal( " + str(column+1) + ", 0, 0, " +
                str(rightWorld[column]) + " ).\n")

    f.write("\n\n")
    for column in xrange(size):
        f.write("rajoyAndCospedal( " + str(column+1) + ", 1, 0, " +
                str(leftWorld[column]) + " ).\n")

    f.write("\n\n")
    for column in xrange(size):
        f.write("rajoyAndCospedal( " + str(column+1) + ", 0, 1, " +
                str(leftWorld[column]) + " ).\n")

    f.write("\n\n")
    for column in xrange(size):
        f.write("rajoyAndCospedal( " + str(column+1) + ", 1, 1, " +
                str(rightWorld[column]) + " ).\n")

def barcenasLeft(size):
    world = createWorld(size)
    leftWorld = list()

    for y in reversed(xrange(size)):
        for x in xrange(size):
            world[x][y] = 0

        leftWorld.insert(0,copy.deepcopy(world))

    return leftWorld

def barcenasRight(size):
    world = createWorld(size)
    rightWorld = list()

    for y in xrange(size):
        for x in xrange(size):
            world[x][y] = 0

        rightWorld.append(copy.deepcopy(world))

    return rightWorld

def setPossibleLocs(x, y, w):
    world = createWorld(w)

    world[x][y] = 0

    if y+1 < size:
        world[x][y+1] = 0
    if y-1 >= 0:
        world[x][y-1] = 0
    if x+1 < size:
        world[x+1][y] = 0
    if x-1 >= 0:
        world[x-1][y] = 0

    return world

def reverseWorld(pl, size):
    for x in xrange(size):
        for y in xrange(size):
            if pl[x][y] == 0:
                pl[x][y] = 1
            else:
                pl[x][y] = 0

    pl[0][0] = 0
    return pl

def createWorld(n):
    world = [[1 for x in xrange(n)] for y in xrange(n)]
    world[0][0] = 0
    return world

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: ./barcenas.py [world size] [sequence of steps]"
    else:
        size = int(sys.argv[1])
        f = open("barcenas.pl", 'w')
        f.truncate()

        intersectLocInfo(f)
        isBarcenasAround(f, size)
        rajoyAndCospedal(f, size)

        f.close()
