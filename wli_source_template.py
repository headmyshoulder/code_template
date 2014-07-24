#! /usr/bin/python

import helpers
import copyright_notes

filename_help = "Output file name(s)"
template = """// Copyright 2012-2014 Wonderlamp Industries GmbH, Potsdam.

#include <iostream>


namespace wli {


} // namespace wli
"""



class wli_source_template():
    
    def __init__( self , name , description ):
        self.name = name
        self.description = description
        self.path = [ "wli" ]
        
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
                f = helpers.full_join( p );
                replacements[ "FILENAME" ] = f
                helpers.default_processing( filename , replacements , template )
