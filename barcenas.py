#!/usr/bin/python

import sys
import copy
import os


def module(f):
    f.write(":- use_module(library(lists)).\n\n\n\n\n")


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


"""
Sets the location for when barcenas is around or not.
"""
def isBarcenasAround(f, size):
    possibleLocs = list()
    for x in xrange(size):
        for y in xrange(size):
            world = setPossibleLocs(x, y, size)
            possibleLocs.append(world)
            f.write("isBarcenasAround( " + str(x+1) + ", " + str(y+1) +
                    ", 0, " + str(world) + " ).\n")
    f.write("\n\n")
    pos = 0
    for x in xrange(size):
        for y in xrange(size):
            reversedWorld = reverseWorld(possibleLocs[pos], size)
            f.write("isBarcenasAround( " + str(x+1) + ", " + str(y+1) + ", 1, "
                    + str(reversedWorld) + " ).\n")
            pos += 1

    f.write("\n\n")


"""
Sets the diferent situations for each response given by Rajoy and Cospedal
even if they are not found.
"""
def rajoyAndCospedal(f, size):
    leftWorld = barcenasLeft(size)
    rightWorld = barcenasRight(size)
    world = createWorld(size)

    """Rajoy or Cospedal not found, everything stays the same."""
    f.write("rajoyAndCospedal( _, -1, _, " + str(world) + " ).\n")
    f.write("rajoyAndCospedal( _, _, -1, " + str(world) + " ).\n\n\n")

    """Mariano sais right, cospedal sais not lying."""
    for column in xrange(size):
        f.write("rajoyAndCospedal( " + str(column+1) + ", 0, 0, " +
                str(rightWorld[column]) + " ).\n")

    f.write("\n\n")

    """Mariano sais left, cospedal sais not lying."""
    for column in xrange(size):
        f.write("rajoyAndCospedal( " + str(column+1) + ", 1, 0, " +
                str(leftWorld[column]) + " ).\n")

    f.write("\n\n")

    """Mariano sais left, cospedal sais lying."""
    for column in xrange(size):
        f.write("rajoyAndCospedal( " + str(column+1) + ", 0, 1, " +
                str(leftWorld[column]) + " ).\n")

    f.write("\n\n")

    """Mariano sais right, cospedal sais lying."""
    for column in xrange(size):
        f.write("rajoyAndCospedal( " + str(column+1) + ", 1, 1, " +
                str(rightWorld[column]) + " ).\n")

    f.write("\n\n")


"""
Updates the information about Rajoy if he its found or not.
"""
def rajoyInfo(f):
    f.write("rajoyInfo( RajoyY, RajoyAns, _, -1, RajoyY, RajoyAns )\n")
    f.write("rajoyInfo( _, _, RajoyY, RajoyAns, RajoyY, RajoyAns )\n\n\n")


"""
Updates the information about Cospedal if she is found or not.
"""
def cospedalInfo(f):
    f.write("cospedalInfo( CospedalAns, -1, CospedalAns )\n")
    f.write("cospedalInfo( _, CospedalAns, CospedalAns )\n\n\n")


def execSeqofSteps(f):
    f.write("execSeqofSteps(PrevLocs, [], _, _, _, PrevLocs).\n")

    f.write("execSeqofSteps(PrevLocs, [[X,Y,S,M,C]|RS], PasY, PasM, PasC, " +
            " FinalLocs\n")
    f.write("    :-\n")
    f.write("        updateSequenceOfSteps(PrevLocs, [X, Y, S, M, C], PasY, " +
            "PasM, PasC, NewLocs),\n")
    f.write("        execSeqofSteps(NewLocs, RS, FinalLocs).\n\n\n")


"""
"""
def updateSequenceOfSteps(f):
    f.write("updateSequenceOfSteps( S0, SequenceOfSteps, PasY, PasM, PasC, SF )\n")
    f.write("   :-\n")
    f.write("      nth0( 0, SequenceOfSteps, X ),\n")
    f.write("      nth0( 1, SequenceOfSteps, Y ),\n")
    f.write("      nth0( 2, SequenceOfSteps, S ),\n")
    f.write("      nth0( 3, SequenceOfSteps, M ),\n")
    f.write("      nth0( 4, SequenceOfSteps, C ),\n")
    f.write("      write( 'Result Pas: ' ), write( [X,Y,S,M,C ] ), nl.\n")
    f.write("      isBarcenasAround( X, Y, S, NewLocs ),\n")
    f.write("      intersectLocs( PrevLocs, NewLocs, FinalLocs ), !,\n")
    """"""""""""""""""""""""""""""""""""""""""
    f.write("      rajoyInfo( PasY, PasM, Y, M, FutY, FutM ),\n")
    f.write("      cospedalInfo( PasC, C, FutC ),\n")
    f.write("      rajoyAndCospedal( FutY, FutM, FutC, RCLocs),\n")
    """"""""""""""""""""""""""""""""""""""""""
    f.write("      intersectLocs( FinalLocs, RCLocs, FinalLocs ), !,\n")
    f.write("      reverse(FinalLocs, World),\n")
    f.write("      writeWorld( World ), !,\n\n\n")


"""
Prints the world in form of table.
"""
def writeWorld(f):
    f.write("writeWorld( [] ) :- !.\n")
    f.write("writeWorld( [Row|RestRows] ) :-\n")
    f.write("      write(Row),nl,\n")
    f.write("      writeWorld(RestRows).\n")


"""
Locations where barcenas can be if Rajoy sais left and is not lying or if sais
right and is lying.
"""
def barcenasLeft(size):
    world = createWorld(size)
    leftWorld = list()

    for y in reversed(xrange(size)):
        for x in xrange(size):
            world[x][y] = 0

        leftWorld.insert(0, copy.deepcopy(world))

    return leftWorld


"""
Locations where barcenas can be if Rajoy sais right and is not lying or if sais
left and is lying.
"""
def barcenasRight(size):
    world = createWorld(size)
    rightWorld = list()

    for y in xrange(size):
        if y != 0:
            for x in xrange(size):
                world[x][y-1] = 0

        rightWorld.append(copy.deepcopy(world))

    return rightWorld

"""
Sets locations where Barcenas can't be leaving the ones where he can be.
"""
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


"""
Changes the 1 to 0 an vice versa so we can obtain the locations of Barcenas
given the location where
"""
def reverseWorld(pl, size):
    for x in xrange(size):
        for y in xrange(size):
            if pl[x][y] == 0:
                pl[x][y] = 1
            else:
                pl[x][y] = 0

    pl[0][0] = 0
    return pl


def call(f, n, plFile):
    world = str(createWorld(n))

    line = "execSeqofSteps(" + world + ",[" + sys.argv[2] + "],_,_,_,_)."
    command = "swipl -q -f " + plFile + " -t " + "'" + line + "'"
    os.system(command)

"""
World with dimension NxN.
"""
def createWorld(n):
    world = [[1 for x in xrange(n)] for y in xrange(n)]
    world[0][0] = 0
    return world


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: ./barcenas.py [world size] [sequence of steps]"
    else:
        size = int(sys.argv[1])
        plFile = "findingBarcenas" + str(size) + "x" + str(size) + ".pl"
        f = open(plFile, 'w')
        f.truncate()
        module(f)
        intersectLocInfo(f)
        isBarcenasAround(f, size)
        rajoyAndCospedal(f, size)
        rajoyInfo(f)
        cospedalInfo(f)
        execSeqofSteps(f)
        updateSequenceOfSteps(f)
        writeWorld(f)
        f.close()

        call(f, size, plFile)
