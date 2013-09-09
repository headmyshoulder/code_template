#! /usr/bin/python

import os

import helpers
import copyright_notes

filename_help = "Output file name(s)"
namespace_help = "Namespace definitions to be created."
class_help = "Class templates to be created" 
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


#ifndef ${FILENAMECAP}_INCLUDED
#define ${FILENAMECAP}_INCLUDED


$NAMESPACE_OPENING

$CLASS_TEMPLATE

$NAMESPACE_CLOSING

#endif // ${FILENAMECAP}_INCLUDED
"""



class odeint_class_template():
    
    def __init__( self ):
        self.name = "OdeintHeader"
        self.description = "Creates a header file with header guards and namespace defintions for odeint."
        self.namespace = [ "boost" , "numeric" , "odeint" ]
        self.path = [ "boost" , "numeric" , "odeint" ]
        
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





