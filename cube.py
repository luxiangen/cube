#coding=utf-8

import random
import sys

order = 3

argc = len( sys.argv )
if argc == 2 :
    order = int( sys.argv[1] )
    
# F : Front
Surf_F = [ ( ['F'] * order ) for i in range( order ) ]
# B : Back
Surf_B = [ ( ['B'] * order ) for i in range( order ) ]
# U : Up
Surf_U = [ ( ['U'] * order ) for i in range( order ) ]
# D : Down
Surf_D = [ ( ['D'] * order ) for i in range( order ) ]
# L : Left
Surf_L = [ ( ['L'] * order ) for i in range( order ) ]
# R : Right
Surf_R = [ ( ['R'] * order ) for i in range( order ) ]

def rotate( surf ) :
    t = 0
    l = 0
    b = len(surf) - 1
    r = len(surf[0]) - 1
    while t < b :
        for i in range( r - l ) :
            tmp = surf[t][l+i]
            surf[t][l+i] = surf[b-i][l]
            surf[b-i][l] = surf[b][r-i]
            surf[b][r-i] = surf[t+i][r]
            surf[t+i][r] = tmp
        t += 1
        l += 1
        b -= 1
        r -= 1

def rotate_X( ) :
    global Surf_B
    global Surf_F
    global Surf_L
    global Surf_R
    global Surf_U
    global Surf_D
    # deal with L and R
    rotate( Surf_R )
    rotate( Surf_L )
    rotate( Surf_L )
    rotate( Surf_L )
    # deal with other surfaces
    rotate( Surf_B )
    rotate( Surf_B )
    tmp = Surf_F
    Surf_F = Surf_D
    Surf_D = Surf_B
    Surf_B = Surf_U
    Surf_U = tmp
    rotate( Surf_B )
    rotate( Surf_B )

def rotate_Y( ) :
    global Surf_B
    global Surf_F
    global Surf_L
    global Surf_R
    global Surf_U
    global Surf_D
    # deal with U and D
    rotate( Surf_U )
    rotate( Surf_D )
    rotate( Surf_D )
    rotate( Surf_D )
    # deal with other surfaces
    tmp = Surf_F
    Surf_F = Surf_R
    Surf_R = Surf_B
    Surf_B = Surf_L
    Surf_L = tmp
    
def rotate_Z( ) :
    global Surf_B
    global Surf_F
    global Surf_L
    global Surf_R
    global Surf_U
    global Surf_D
    # deal with F and B
    rotate( Surf_F )
    rotate( Surf_B )
    rotate( Surf_B )
    rotate( Surf_B )
    # deal with other surfaces
    tmp = Surf_U
    Surf_U = Surf_L
    Surf_L = Surf_D
    Surf_D = Surf_R
    Surf_R = tmp
    rotate( Surf_U )
    rotate( Surf_L )
    rotate( Surf_D )
    rotate( Surf_R )

def rotate_up( ) :
    rotate( Surf_U )
    tmp = Surf_L[0]
    Surf_L[0] = Surf_F[0]
    Surf_F[0] = Surf_R[0]
    Surf_R[0] = Surf_B[0]
    Surf_B[0] = tmp

def rotate_down( ) :
    rotate_X()
    rotate_X()
    rotate_up()
    rotate_X()
    rotate_X()

def rotate_front( ) :
    rotate_X()
    rotate_up()
    rotate_X()
    rotate_X()
    rotate_X()

def rotate_back( ) :
    rotate_X()
    rotate_X()
    rotate_X()
    rotate_up()
    rotate_X()

def rotate_left( ) :
    rotate_Z()
    rotate_up()
    rotate_Z()
    rotate_Z()
    rotate_Z()

def rotate_right( ) :
    rotate_Z()
    rotate_Z()
    rotate_Z()
    rotate_up()
    rotate_Z()

def do_rotate( action ) :
    switch = {
        "F" : rotate_front,
        "B" : rotate_back,
        "U" : rotate_up,
        "D" : rotate_down,
        "L" : rotate_left,
        "R" : rotate_right,
        "X" : rotate_X,
        "Y" : rotate_Y,
        "Z" : rotate_Z
    }
    try:
        switch[ action ]()
    except KeyError as e:
        pass

def do_rotates( actions ) :
    actions = actions.replace( 'f', 'FFF' )
    actions = actions.replace( 'r', 'RRR' )
    actions = actions.replace( 'l', 'LLL' )
    actions = actions.replace( 'u', 'UUU' )
    actions = actions.replace( 'b', 'BBB' )
    actions = actions.replace( 'd', 'DDD' )
    actions = actions.replace( 'x', 'XXX' )
    actions = actions.replace( 'y', 'YYY' )
    actions = actions.replace( 'z', 'ZZZ' )
    for action in actions :
        do_rotate( action )

def show_cube() :
    print( '-' * 4 * (order*2+1) ) 
    for i in range(order) :
        print( "  "*order, end = '  ' )
        for j in range(order) :
            print( Surf_U[i][j], end=' ' )
            #color.show_text( Surf_U[i][j], F_RED )
        print( '' )
    print( '' )
   
    for i in range(order) :
        for j in range(order) :
            print( Surf_L[i][j], end = ' ' )
        print( "  ", end = '' )
        for j in range(order) :
            print( Surf_F[i][j], end = ' ' )
        print( "  ", end = '' )
        for j in range(order) :
            print( Surf_R[i][j], end = ' ' )
        print( "  ", end = '' )
        for j in range(order) :
            print( Surf_B[i][j], end = ' ' )
        print( '' )
    print( '' )
    
    for i in range(order) :
        print( "  "*order, end = '  ' )
        for j in range(order) :
            print( Surf_D[i][j], end =' ' )
        print( '' )
    print( '-' * 4 * (order*2+1) ) 
    print( '' )

def usage() :
    print( "h/help   : Show this usage" )
    print( "random   : Shuffle the magic cube" )
    print( "q/Q/exit : Quit" )
    print( "Multiple commands can be used for below actions:" )
    print( "    U/u  : Rotate the Up    surface clockwise / anti-clockwise" )
    print( "    D/d  : Rotate the Down  surface clockwise / anti-clockwise" )
    print( "    L/l  : Rotate the Left  surface clockwise / anti-clockwise" )
    print( "    R/r  : Rotate the Right surface clockwise / anti-clockwise" )
    print( "    F/f  : Rotate the Front surface clockwise / anti-clockwise" )
    print( "    B/b  : Rotate the Back  surface clockwise / anti-clockwise" )
    print( "    X/x  : Rotate the Magic cube along X-axis clockwise / anti-clockwise" )
    print( "    Y/y  : Rotate the Magic cube along Y-axis clockwise / anti-clockwise" )
    print( "    Z/z  : Rotate the Magic cube along Z-axis clockwise / anti-clockwise" )
    print( "    For example, we can input : RUrURUUr or RuRURURuruRR" )

usage()
show_cube()

while True :
    s = input( "> " )
    if s == "q" or s == "Q" or s == "exit":
        break
    elif s == "h" or s == "help" :
        usage()
    elif s == "random" :
        for i in range(100) :
            for c in random.sample("LURDFB", 3 ) :
                do_rotates( c )
    else:
        do_rotates( s )
    show_cube()
    

    
