#! /usr/bin/python

import os
import subprocess

import helpers


project_help = "Project name to be created. The project folder will be names like this."
sourcefiles_help = "Source cpp files to be created."
mainfiles_help = "Main cpp files to be created."
headerfiles_help = "Header files to be created."
# license_help = "License type"


def run( arg ):
    devnull = open( '/dev/null' , 'w' )
    proc = subprocess.Popen( arg , stdout=devnull )
    ret = proc.wait()
    if ret != 0 :
        print "Error while " + str( arg )
    
        
class cpp_project_template():
    
    def __init__( self ):
        self.name = "CppProject"
        self.description = "Cpp project with CMakelists.txt and several source and header files."

    def register_in_arg_parser( self , subparsers ):
        parser = helpers.create_subparser( self , subparsers )
        parser.add_argument( "project" , help = project_help )
        parser.add_argument( "-s" , "--sourcefiles" , nargs = "*" , help = sourcefiles_help )
        parser.add_argument( "-m" , "--mainfiles" , nargs = "*" , help = mainfiles_help )
        parser.add_argument( "-i" , "--headerfiles" , nargs = "*" , help = headerfiles_help )
        # parser.add_argument( "-l" , "--license" , nargs=1 , help = license_help , default = "no" , choices = copyright_notes.copyrights.keys() )

    def do_work( self , args , replacements ):
        print "Creating " + self.name + " template(s) ..."

        print "* Creating project folder"
        os.mkdir( args.project )
        print "* Switching to project folder"
        os.chdir( args.project )
        print "* Creating build folder"
        os.mkdir( "build" )
        print "* Creating header folder"
        os.mkdir( "include" )
        os.mkdir( "include/" + args.project )
        print "* Creating test folder"
        os.mkdir( "test" )
        print "* Creating examples folder"
        os.mkdir( "examples" )
        print "* Creating doc folder"
        os.mkdir( "doc" )
        print "* Creating src folder"
        os.mkdir( "src" )

        cmake_str = [ "code_template.py" , "SimpleCMake" , "-p" , args.project ]
        if( hasattr( args , "mainfiles" ) ) and ( args.mainfiles is not None ) and ( len( args.mainfiles ) != 0 ) :
            cmake_str.append( "-t" )
            for m in args.mainfiles :
                print "* Creating main file " + m 
                run( [ "code_template.py" , "SimpleMain" , m ] )
                cmake_str.append( m )
        
        if( hasattr( args , "headerfiles" ) ) and ( args.headerfiles is not None ) and ( len( args.headerfiles ) != 0 ) :
            for h in args.headerfiles:
                print "* Creating header file " + h
                run( [ "code_template.py" , "SimpleHeader" , "-f" , h ] )

        
        if( hasattr( args , "sourcefiles" ) ) and ( args.sourcefiles is not None ) and ( len( args.sourcefiles ) != 0 ) :
            for s in args.sourcefiles :
                print "* Creating source file " + s
                run( [ "code_template.py" , "SimpleSource" , s ] )

        print "Creating CMakelists.txt"
        run( cmake_str )
