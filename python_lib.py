#! /usr/bin/python

import os

import helpers
import copyright_notes

filename_help = "Output python name(s)"

template = """#! /usr/bin/python

\"\"\" $FILENAME \"\"\"
 
__date__ = "$DATE"
__author__ = "$AUTHOR"
__email__ = "$AUTHOREMAIL"

import unittest

def dummyFunc():
    return 1
    
class DummyTest( unittest.TestCase ):
    def testDummyFunc( self ):
        self.assertEqual( 1 , dummyFunc() )

if __name__ == "__main__" :
    unittest.main()
"""


class python_lib_template():
    
    def __init__( self , name , description , path = [] ):
        self.name = name
        self.description = description
        self.path = path
        
    def register_in_arg_parser( self , subparsers ):
        parser = helpers.create_subparser( self , subparsers )
        parser.add_argument( "filename" ,  nargs = "+" , help = filename_help )
        

    def do_work( self , args , replacements ):
        print "Creating " + self.name + " template(s) ..."
        
        path = helpers.find_path( self.path )
        
        if hasattr( args , "filename" ) :
            for filename in args.filename:
                p = path
                p.append( filename )
                f = helpers.full_join( p )
                helpers.add_filename_replacements( replacements , filename )
                replacements[ "FILENAME" ] = f
                helpers.default_processing( filename , replacements , template )
