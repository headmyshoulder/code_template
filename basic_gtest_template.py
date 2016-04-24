#! /usr/bin/python

import os

import helpers
import copyright_notes

filename_help = "Output file name(s)"
test_help = "Name of the test."
template = """/*
 * $FILENAME
 * Date: $DATE
 * Author: $AUTHOR ($AUTHOREMAIL)
 * Copyright: $AUTHOR
 *
$LICENSE
 */

#include <gtest/gtest.h>

#define TESTNAME $TESTNAME

using namespace std;

TEST( TESTNAME , test_case )
{
    EXPECT_EQ( true , true );
}
"""



class basic_gtest_template():
    
    def __init__( self , name , description , path = [] , license = copyright_notes.boost_copyright_for_header ):
        self.name = name
        self.description = description
        self.license = license
        self.path = path
        
    def register_in_arg_parser( self , subparsers ):
        parser = helpers.create_subparser( self , subparsers )
        parser.add_argument( "filename" ,  nargs = "+" , help = filename_help )
        parser.add_argument( "-t" , "--test" , nargs = 1 , help = test_help )


    def do_work( self , args , replacements ):
        print "Creating " + self.name + " template(s) ..."
        
        path = helpers.find_path( self.path )
        
        replacements[ "LICENSE" ] = self.license
        replacements[ "TESTNAME" ] = "dummy"
        
        if hasattr( args , "test" ) and ( args.test is not None ) and ( len( args.test ) == 1 ):
            print "Found test " + args.test[0]
            replacements[ "TESTNAME" ] = args.test[0]


        if hasattr( args , "filename" ) :
            for filename in args.filename:
                filename = helpers.check_filename_ending( filename , "cpp" )
                p = path
                p.append( filename )
                f = helpers.full_join( p )
                replacements[ "FILENAME" ] = f
                helpers.default_processing( filename , replacements , template )
