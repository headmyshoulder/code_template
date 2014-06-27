#! /usr/bin/python

import os

import helpers
import copyright_notes

filename_help = "Output file name(s)"
namespace_help = "Namespace definitions to be created."
class_help = "Class templates to be created" 
template = """// Copyright 2014 Wonderlamp Industries GmbH, Potsdam.

#ifndef ${FILENAMECAP}
#define ${FILENAMECAP} 1


$NAMESPACE_OPENING

$CLASS_TEMPLATE

$NAMESPACE_CLOSING

#endif // ${FILENAMECAP}
"""



class wli_header_template():
    
    def __init__( self , name , description ):
        self.name = name
        self.description = description
        self.libname = "wli"
        self.namespace = [ "wli" ]
        self.path = [ "wli" ] 
        
    def register_in_arg_parser( self , subparsers ):
        parser = helpers.create_subparser( self , subparsers )
        parser.add_argument( "-f" , "--filename" ,  nargs = "+" , help = filename_help , required=True )
        parser.add_argument( "-n" , "--namespace" , nargs = "*" , help = namespace_help )
        parser.add_argument( "-c" , "--class" , nargs = "*" , help = class_help , dest = "classes" )


    def do_work( self , args , replacements ):
        print "Creating " + self.name + " template(s) ..."
        
        path = helpers.find_path( self.path )

        helpers.add_namespace_replacements( replacements , args , self.namespace )
        helpers.add_class_replacements( replacements , args , helpers.default_class_template )
        replacements[ "LIBNAME" ] = self.libname.upper()
        
        if hasattr( args , "filename" ) :
            for filename in args.filename:
                filename = helpers.check_filename_ending( filename , "hpp" )
                p = path
                p.append( filename )
                f = helpers.full_join( p )
                helpers.add_filename_replacements( replacements , filename )
                replacements[ "FILENAME" ] = f
                ff = f
                if ff.count( "src" ) != 0:
                    ff = ff[ ff.index( "src" ) + 4 : ]
                replacements[ "FILENAMECAP" ] = helpers.create_cap_filename_str( ff )
                helpers.default_processing( filename , replacements , template )

