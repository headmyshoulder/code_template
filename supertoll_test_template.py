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
 */

#include <cppunit/config/SourcePrefix.h>
#include <cppunit/extensions/HelperMacros.h>

#define TESTNAME $TESTNAME


class TESTNAME : public CPPUNIT_NS::TestFixture
{
    CPPUNIT_TEST_SUITE( TESTNAME );

    CPPUNIT_TEST( test1 );

    CPPUNIT_TEST_SUITE_END();

public:

    void setUp( void )
    {
    }

    void tearDown( void )
    {
    }


protected:

    void test1( void )
    {
        CPPUNIT_ASSERT( true );
    }

};

CPPUNIT_TEST_SUITE_REGISTRATION( TESTNAME );
"""


        



class supertoll_test_template():
    
    def __init__( self ):
        self.path = [ "UnitTest" ]
        self.name = "SuperTollTest"
        self.description = "Creates a SuperToll test file."

    def register_in_arg_parser( self , subparsers ):
        parser = helpers.create_subparser( self , subparsers )
        parser.add_argument( "filename" ,  nargs = "+" , help = filename_help )
        parser.add_argument( "-t" , "--test" , nargs = 1 , help = test_help )

    def do_work( self , args , replacements ):
        print "Creating " + self.name + " template(s) ..."

        path = helpers.find_path( self.path )

        replacements[ "TESTNAME" ] = "dummy"
        if hasattr( args , "test" ) and ( args.test is not None ) and ( len( args.test ) == 1 ):
            print "Found test " + args.test[0]
            replacements[ "TESTNAME" ] = args.test[0]

        if hasattr( args , "filename" ) :
            for filename in args.filename:
                filename = helpers.check_filename_ending( filename , "cpp" )
                p = path
                p.append( filename )
                replacements[ "FILENAME" ] = helpers.full_join( p )
                helpers.default_processing( filename , replacements , template )
