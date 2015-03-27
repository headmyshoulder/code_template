#! /usr/bin/python

import os

import helpers
import copyright_notes

filename_help = "Output python name(s)"
postgres_help = "Include postgres in argument parser."

template = """#! /usr/bin/python

\"\"\" $FILENAME \"\"\"
 
__date__ = "$DATE"
__author__ = "$AUTHOR"
__email__ = "$AUTHOREMAIL"


$INCLUDES


$ARGPARSE


$MAIN

if __name__ == "__main__" :
    main( sys.argv )

"""

argparsetemplate = """def parseCmd( argv ):
    parser = argparse.ArgumentParser( description = "Application description" , formatter_class = argparse.ArgumentDefaultsHelpFormatter )
    addCommonArguments( parser )
    addLogArguments( parser )
    args = parser.parse_args( argv[1:] )
    return args"""
    
    
argparsetemplatedb = """def parseCmd( argv ):
    parser = argparse.ArgumentParser( description = "Application description" , formatter_class = argparse.ArgumentDefaultsHelpFormatter )
    addCommonArguments( parser )
    addLogArguments( parser )
    addDatabaseArguments( parser )
    args = parser.parse_args( argv[1:] )
    return args"""

    
    
includes = """from SuperToll.Util.CmdLineArguments import *
from SuperToll.Util.InitLogging import *

import sys
import argparse
import logging
"""

main = """def main( argv ):
    args = parseCmd( argv )
    initLogging( args )
"""

class supertoll_python_application_template():
    
    def __init__( self , name , description , path = [] ):
        self.name = name
        self.description = description
        self.path = path
        
    def register_in_arg_parser( self , subparsers ):
        parser = helpers.create_subparser( self , subparsers )
        parser.add_argument( "filename" ,  nargs = "+" , help = filename_help )
        parser.add_argument( "-p" , "--postgres" , action="store_true" , help = postgres_help )
        

    def do_work( self , args , replacements ):
        print "Creating " + self.name + " template(s) ..."
        
        path = helpers.find_path( self.path )
        
        replacements[ "INCLUDES" ] = includes
        replacements[ "MAIN" ] = main

        if args.postgres :
            replacements[ "INCLUDES" ] += "import psycopg2"
            replacements[ "ARGPARSE" ] = argparsetemplatedb
            replacements[ "MAIN" ] += """\n    logging.info( "Connect to db " + args.dbname )
    db = psycopg2.connect( host=args.dbhost , port=args.dbport , database=args.dbname , user=args.dbuser , password=args.dbpw )"""
            
        if not args.postgres :
            replacements[ "ARGPARSE" ] = argparsetemplate

        if hasattr( args , "filename" ) :
            for filename in args.filename:
                p = path
                p.append( filename )
                f = helpers.full_join( p )
                helpers.add_filename_replacements( replacements , filename )
                replacements[ "FILENAME" ] = f
                helpers.default_processing( filename , replacements , template )
