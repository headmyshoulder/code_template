#! /usr/bin/python

import helpers
import copyright_notes

filename_help = "Output file name(s)"
template = """/*
 * $FILENAME
 * Date: $DATE
 * Author: $AUTHOR ($AUTHOREMAIL)
 * Copyright: $AUTHOR
 *
$LICENSE
 */


#include <iostream>

using namespace std;


int main( int argc , char *argv[] )
{
    cout << "Hello world!" << endl;
    return 0;
}
"""



class basic_main_template():
    
    def __init__( self , name , description , path = [] , license = copyright_notes.boost_copyright_for_header ):
        self.name = name
        self.description = description
        self.license = license
        self.path = path
        
    def register_in_arg_parser( self , subparsers ):
        parser = helpers.create_subparser( self , subparsers )
        parser.add_argument( "filename" ,  nargs = "+" , help = filename_help )


    def do_work( self , args , replacements ):
        print "Creating " + self.name + " template(s) ..."
        
        path = helpers.find_path( self.path )
        replacements[ "LICENSE" ] = self.license

        if hasattr( args , "filename" ) :
            for filename in args.filename:
                filename = helpers.check_filename_ending( filename , "cpp" )
                p = path
                p.append( filename )
                f = helpers.full_join( p );
                replacements[ "FILENAME" ] = f
                helpers.default_processing( filename , replacements , template )
