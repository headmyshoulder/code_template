#! /usr/bin/python

import os

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

template_pragma_once = """/*
 * $FILENAME
 * Date: $DATE
 * Author: $AUTHOR ($AUTHOREMAIL)
 * Copyright: $AUTHOR
 *
$LICENSE
 */

#pragma once

$NAMESPACE_OPENING

$CLASS_TEMPLATE

$NAMESPACE_CLOSING
"""



class basic_header_template():
    
    def __init__( self , name , description , libname , namespace , path , use_pragma_once = False , license = copyright_notes.boost_copyright_for_header ):
        self.name = name
        self.description = description
        self.libname = libname
        self.license = license
        self.namespace = namespace 
        self.path = path
        self.use_pragma_once = use_pragma_once
        
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
                if self.use_pragma_once:
                    helpers.default_processing( filename , replacements , template_pragma_once )
                else:
                    helpers.default_processing( filename , replacements , template )

