#! /usr/bin/python

import os

import helpers
import copyright_notes

filename_help = "Output python name(s)"
argument_parser_help = "User argument parser."
postgres_help = "Include postgres in argument parser."

template = """#! /usr/bin/python

\"\"\" $FILENAME \"\"\"
 
__date__ = "$DATE"
__author__ = "$AUTHOR"
__email__ = "$AUTHOREMAIL"

import sys
$INCLUDES

$ARGPARSE

$INITLOGGING

def main( argv ):
$MAIN

if __name__ == "__main__" :
    main( sys.argv )

"""

argparsetemplate = """def parseCmd( argv ):
    parser = argparse.ArgumentParser( description = "Application description" )
    parser.add_argument( "-l" , "--logfile" , help="Logile" , default="log.log" )
    args = parser.parse_args( argv[1:] )
    return args"""


argparsetemplatedb = """def parseCmd( argv ):
    parser = argparse.ArgumentParser( description = "Application description" )
    parser.add_argument( "-l" , "--logfile" , help="Logile" , default="log.log" )
    parser.add_argument( "--dbname" , help="database name" , default="db" )
    parser.add_argument( "--dbhost" , help="database host" , default="localhost" )
    parser.add_argument( "--dbport" , help="database port" , default=5432 )
    parser.add_argument( "--dbuser" , help="database user" , default="user" )
    parser.add_argument( "--dbpw" , help="database user" , default="pw" )
    args = parser.parse_args( argv[1:] )
    return args"""

initlogging = """def initLogging( args ):
    formatString = '[%(levelname)s][%(asctime)s] : %(message)s'
    # formatString = '[%(levelname)s][%(name)s] : %(message)s'
    logLevel = logging.INFO
    logging.basicConfig( format=formatString , level=logLevel , datefmt='%Y-%m-%d %I:%M:%S')
    ch = logging.FileHandler( args.logfile , "w" )
    ch.setLevel( logLevel )
    ch.setFormatter( logging.Formatter( formatString , datefmt='%Y-%m-%d %I:%M:%S') )
    logging.getLogger().addHandler( ch )"""

maintemplateargsdb = """    args = parseCmd( argv )
    initLogging( args )
    logging.info( "Connect to db " + args.dbname )
    db = psycopg2.connect( host=args.dbhost , port=args.dbport , database=args.dbname , user=args.dbuser , password=args.dbpw )"""
    
maintemplateargs = """    args = parseCmd( argv )
    initLogging( args )"""
    
maintemplateempty = """    pass"""

class python_application_template():
    
    def __init__( self , name , description , path = [] ):
        self.name = name
        self.description = description
        self.path = path
        
    def register_in_arg_parser( self , subparsers ):
        parser = helpers.create_subparser( self , subparsers )
        parser.add_argument( "filename" ,  nargs = "+" , help = filename_help )
        parser.add_argument( "-a" , "--args" , action="store_true" , help = argument_parser_help )
        parser.add_argument( "-p" , "--postgres" , action="store_true" , help = postgres_help )
        

    def do_work( self , args , replacements ):
        print "Creating " + self.name + " template(s) ..."
        
        path = helpers.find_path( self.path )
        
        if args.args and args.postgres :
            replacements[ "INCLUDES" ] = "import argparse\nimport logging\nimport psycopg2"
            replacements[ "ARGPARSE" ] = argparsetemplatedb
            replacements[ "INITLOGGING" ] = initlogging
            replacements[ "MAIN" ] = maintemplateargsdb
            
        if args.args and not args.postgres :
            replacements[ "INCLUDES" ] = "import argparse\nimport logging"
            replacements[ "ARGPARSE" ] = argparsetemplate
            replacements[ "INITLOGGING" ] = initlogging
            replacements[ "MAIN" ] = maintemplateargs
            
        if not args.args :
            replacements[ "INCLUDES" ] = ""
            replacements[ "ARGPARSE" ] = ""
            replacements[ "INITLOGGING" ] = ""
            replacements[ "MAIN" ] = "    pass"

        
        if hasattr( args , "filename" ) :
            for filename in args.filename:
                p = path
                p.append( filename )
                f = helpers.full_join( p )
                helpers.add_filename_replacements( replacements , filename )
                replacements[ "FILENAME" ] = f
                helpers.default_processing( filename , replacements , template )
