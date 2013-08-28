#! /usr/bin/python

import os

from string import Template

import helpers


filename_help = "Output file name(s)"
namespace_help = "Namespace definitions to be created."
class_help = "Class templates to be created" 
template = """/*
 * $FILENAME
 * Date: $DATE
 * Author: $AUTHOR ($AUTHOREMAIL)
 * Copyright: $AUTHOR
 *

 */

#ifndef ${LIBNAME}_${FILENAMECAP}_${FILEENDINGCAP}_INCLUDED
#define ${LIBNAME}_${FILENAMECAP}_${FILEENDINGCAP}_INCLUDED


$NAMESPACE_OPENING

$CLASS_TEMPLATE

$NAMESPACE_CLOSING

#endif // ${LIBNAME}_${FILENAMECAP}_${FILEENDINGCAP}_INCLUDED
"""



class basic_class_template():
    
    def __init__( self , libname ):
        self.libname = libname
        
    def register_in_arg_parser( self , plugin , subparsers ):
        parser = helpers.create_subparser( plugin , subparsers )
        parser.add_argument( "-f" , "--filename" ,  nargs = "+" , help = filename_help , required=True )
        parser.add_argument( "-n" , "--namespace" , nargs = "*" , help = namespace_help )
        parser.add_argument( "-c" , "--class" , nargs = "*" , help = class_help , dest = "classes" )


    def do_work( self , plugin , args , replacements ):
        print "Creating " + plugin.name + " template(s) ..."

        helpers.add_namespace_replacements( replacements , args , [ "Amboss" ] )
        helpers.add_class_replacements( replacements , args , helpers.default_class_template )
        replacements[ "LIBNAME" ] = self.libname.upper()
        
        if hasattr( args , "filename" ) :
            for filename in args.filename:
                filename = helpers.check_filename_ending( filename , "h" )
                helpers.default_processing( filename , replacements , template )
