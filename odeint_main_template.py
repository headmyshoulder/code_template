#! /usr/bin/python

import os

import helpers
import copyright_notes


filename_help = "Output file name(s)"
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

#include <boost/numeric/odeint.hpp>

#include <iostream>

namespace odeint = boost::numeric::odeint;

int main( int argc , char *argv[] )
{
    std::cout << "Hello world!" << std::endl;
    return 0;
}
"""


        



class odeint_main_template():
    
    def __init__( self ):
        self.path = [ "libs" , "numeric" , "odeint" ]
        self.name = "OdeintMain"
        self.description = "Creates a source file (example) for odeint."

    def register_in_arg_parser( self , subparsers ):
        parser = helpers.create_subparser( self , subparsers )
        parser.add_argument( "filename" ,  nargs = "+" , help = filename_help )

    def do_work( self , args , replacements ):
        print "Creating " + self.name + " template(s) ..."

        path = helpers.find_path( self.path )


        if hasattr( args , "filename" ) :
            for filename in args.filename:
                filename = helpers.check_filename_ending( filename , "cpp" )
                p = path
                p.append( filename )
                replacements[ "FILENAME" ] = helpers.full_join( p )
                helpers.default_processing( filename , replacements , template )
