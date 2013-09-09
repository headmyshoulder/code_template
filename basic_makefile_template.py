#! /usr/bin/python

import os

import helpers
import copyright_notes

filename_help = "Output file name(s)"
target_help = "Cpp targets to be created."
project_help = "Project name to be created."

template = """# $FILENAME
# Date: $DATE
# Author: $AUTHOR ($AUTHOREMAIL)
#
$LICENSE

CC = g++
CXX = g++

INCLUDES = -I$$(BOOST_ROOT)
CXXFLAGS += $$(INCLUDES)

all : $TARGET

$TARGETS

clean :
\trm *.o *~ $TARGET
"""



class basic_makefile_template():
    
    def __init__( self , name , description , path = [] , license = copyright_notes.boost_copyright_for_python ):
        self.name = name
        self.description = description
        self.license = license
        self.path = path
        
    def register_in_arg_parser( self , subparsers ):
        parser = helpers.create_subparser( self , subparsers )
        parser.add_argument( "-f" , "--filename" ,  nargs = "+" , help = filename_help , default=[ "Makefile" ] )
        parser.add_argument( "-t" , "--target" , nargs = "*" , help = target_help )

    def do_work( self , args , replacements ):
        print "Creating " + self.name + " template(s) ..."
        
        path = helpers.find_path( self.path )
        
        replacements[ "LICENSE" ] = self.license
        
        replacements[ "TARGET" ] = ""
        replacements[ "TARGETS" ] = ""
        if ( hasattr( args , "target" ) ) and ( args.target is not None ) and ( len( args.target ) != 0 ) :
            for target in args.target:
                print "* Found target " + target
                replacements[ "TARGET" ] += ( target + " " )
                replacements[ "TARGETS" ] += ( target + " : " + target + ".o" + "\n" )

            
        if hasattr( args , "filename" ) :
            for filename in args.filename:
                p = path
                p.append( filename )
                f = helpers.full_join( p )
                helpers.add_filename_replacements( replacements , filename )
                replacements[ "FILENAME" ] = f
                helpers.default_processing( filename , replacements , template )
