#! /usr/bin/python

import os

import helpers
import copyright_notes


filename_help = "Output file name(s)"
test_help = "Name of the test."
template = """/*
 [auto_generated]
 $FILENAME

 [begin_description]
 tba.
 [end_description]

 Copyright 2009-2012 Karsten Ahnert
 Copyright 2009-2012 Mario Mulansky

 Distributed under the Boost Software License, Version 1.0.
 (See accompanying file LICENSE_1_0.txt or
 copy at http://www.boost.org/LICENSE_1_0.txt)
 */

#include <boost/config.hpp>
#ifdef BOOST_MSVC
    #pragma warning(disable:4996)
#endif

#define BOOST_TEST_MODULE odeint_$TESTNAME

#include <boost/numeric/odeint/stepper/runge_kutta4.hpp>

#include <boost/test/unit_test.hpp>

using namespace boost::unit_test;
using namespace boost::numeric::odeint;


BOOST_AUTO_TEST_SUITE( ${TESTNAME}_test )

BOOST_AUTO_TEST_CASE( test_case1 )
{
    BOOST_CHECK_EQUAL( 1 , 1 );
}

BOOST_AUTO_TEST_SUITE_END()
"""


        



class odeint_test_template():
    
    def __init__( self ):
        self.path = [ "libs" , "numeric" , "odeint" ]
        self.name = "OdeintTest"
        self.description = "Creates a unit test file for odeint.."

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
