#! /usr/bin/python

import os

import helpers
import copyright_notes

filename_help = "Output file name(s)"
target_help = "Cpp targets to be created."
project_help = "Project name to be created."

template = """# $FILENAME
# Date: $DATE
# Author: $AUTHOR ($AUTHOREMAIL)
#
$LICENSE

import boost ;

boost.use-project ;

path-constant TOP : . ;

project 
    : requirements
    <library>/boost//headers
    <library>/boost/program_options//boost_program_options
    <toolset>gcc:<cxxflags>-fno-strict-aliasing
    <toolset>gcc:<cxxflags>--std=c++0x
    ;

$TARGETS
"""



class basic_jamfile_template():
    
    def __init__( self , name , description , path = [] , license = copyright_notes.boost_copyright_for_python ):
        self.name = name
        self.description = description
        self.license = license
        self.path = path
        
    def register_in_arg_parser( self , subparsers ):
        parser = helpers.create_subparser( self , subparsers )
        parser.add_argument( "-f" , "--filename" ,  nargs = "+" , help = filename_help , default=["Jamroot"] )
        parser.add_argument( "-t" , "--target" , nargs = "*" , help = target_help )


    def do_work( self , args , replacements ):
        print "Creating " + self.name + " template(s) ..."
        
        path = helpers.find_path( self.path )
        
        replacements[ "LICENSE" ] = self.license
        replacements[ "TARGETS" ] = ""
        if ( hasattr( args , "target" ) ) and ( args.target is not None ) and ( len( args.target ) != 0 ) :
            for target in args.target:
                print "* Found target " + target
                p = os.path.splitext( target )
                if p[1] == ".cpp" :
                    replacements[ "TARGETS" ] += "exe " + p[0] + " : " + p[0] + ".cpp" + "\n"
                else:
                    replacements[ "TARGETS" ] += "exe " + target + " : " + target + ".cpp" + "\n"
            
        if hasattr( args , "filename" ) :
            for filename in args.filename:
                p = path
                p.append( filename )
                f = helpers.full_join( p )
                helpers.add_filename_replacements( replacements , filename )
                replacements[ "FILENAME" ] = f
                helpers.default_processing( filename , replacements , template )
