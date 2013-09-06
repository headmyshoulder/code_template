#! /usr/bin/python

import os

from string import Template

import helpers
import copyright_notes

filename_help = "Output file name(s)"
namespace_help = "Namespace definitions to be created."
class_help = "Class templates to be created" 
template = """/*
 * $FILENAME
 * Date: $DATE
 * Author: $AUTHOR ($AUTHOREMAIL)
 * Copyright: $AUTHOR
 *
$LICENSE
 */

#ifndef ${FILENAMECAP}_INCLUDED
#define ${FILENAMECAP}_INCLUDED


$NAMESPACE_OPENING

$CLASS_TEMPLATE

$NAMESPACE_CLOSING

#endif // ${FILENAMECAP}_INCLUDED
"""



class basic_class_template():
    
    def __init__( self , libname , namespace , path , license = copyright_notes.boost_copyright_for_header ):
        self.libname = libname
        self.license = license
        self.namespace = namespace 
        self.path = path
        
    def register_in_arg_parser( self , plugin , subparsers ):
        parser = helpers.create_subparser( plugin , subparsers )
        parser.add_argument( "-f" , "--filename" ,  nargs = "+" , help = filename_help , required=True )
        parser.add_argument( "-n" , "--namespace" , nargs = "*" , help = namespace_help )
        parser.add_argument( "-c" , "--class" , nargs = "*" , help = class_help , dest = "classes" )


    def do_work( self , plugin , args , replacements ):
        print "Creating " + plugin.name + " template(s) ..."
        
        path = helpers.find_path( self.path )

        helpers.add_namespace_replacements( replacements , args , self.namespace )
        helpers.add_class_replacements( replacements , args , helpers.default_class_template )
        replacements[ "LIBNAME" ] = self.libname.upper()
        replacements[ "LICENSE" ] = self.license
        
        if hasattr( args , "filename" ) :
            for filename in args.filename:
                filename = helpers.check_filename_ending( filename , "h" )
                p = path
                p.append( filename )
                f = helpers.full_join( p )
                helpers.add_filename_replacements( replacements , filename )
                replacements[ "FILENAME" ] = f
                replacements[ "FILENAMECAP" ] = helpers.create_cap_filename_str( f )
                helpers.default_processing( filename , replacements , template )

