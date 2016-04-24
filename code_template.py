#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import argparse
import argcomplete
import datetime
import os
import glob
import collections

from basic_header_template import *
from basic_source_template import *
from basic_main_template import *
from basic_gtest_template import *
from basic_cmake_template import *
from basic_jamfile_template import *
from basic_makefile_template import *
from odeint_header_template import *
from odeint_main_template import *
from odeint_test_template import *
from supertoll_test_template import *
from simple_cpp_project_template import *
from cpp_project_template import *
from wli_header_template import *
from wli_source_template import *
from python_application import *
from python_lib import *
from supertoll_python_application import *

description = "Create source code templates for commonly used files."

config = {
    "Author" : "Karsten Ahnert" ,
    "AuthorEmail" : "karsten.ahnert@gmx.de"
}

default_replacements = {
    "AUTHOR" : config[ "Author" ] ,
    "AUTHOREMAIL" : config[ "AuthorEmail" ] ,
    "DATE" : datetime.date.today().isoformat()
}


templates = {}

templates[ "AmbossHeader" ] = basic_header_template(
    "AmbossHeader" , 
    "Creates a simple header with header guards for Amboss." ,
    "Amboss" , [ "Amboss" ] , [ "Amboss" ] ) 
templates[ "GPCXXHeader" ] = basic_header_template(
    "GPCXXHeader" ,
    "Creates a header file with header guards and namespace defintions for gpcxx." ,
    "gpcxx" , [ "gpcxx" ] , [ "gpcxx" ] )
templates[ "SimpleHeader" ] = basic_header_template(
    "SimpleHeader" ,
    "Creates a simple header with header guards." ,
    "simple" , [] , [] , license = copyright_notes.no_copyright_for_header )
templates[ "SuperTollHeader" ] = basic_header_template(
    "SuperTollHeader" ,
    "Creates a simple header with header guards for SuperToll." ,
    "SuperToll" , [ "SuperToll" ] , [ "SuperToll" ] , license = copyright_notes.no_copyright_for_header )
templates[ "AModHeader" ] = basic_header_template(
    "AModHeader" ,
    "Creates a simple header with header guards for AMod." ,
    "AMod" , [ "AMod" ] , [ "AMod" ] , license = copyright_notes.no_copyright_for_header )
templates[ "ZEHeader" ] = basic_header_template(
    "ZEHeader" ,
    "Creates a simple header with header guards for ZE." ,
    "ZE" , [ "ZE" ] , [ "ZE" ] , license = copyright_notes.no_copyright_for_header )
templates[ "FormulaHeader" ] = basic_header_template(
    "FormulaHeader" ,
    "Creates a simple header with header guards for formula." ,
    "formula" , [ "formula" ] , [ "formula" ] , use_pragma_once = True , license = copyright_notes.no_copyright_for_header )

#templates[ "NumdiffHeader" ] = basic_header_template(
    #"NumdiffHeader" ,
    #"Creates a header for numdiff" ,
    #"Numdiff" , [ "numdiff" ] , [ "numdiff" ] )
#templates[ "WliHeader" ] = wli_header_template(
    #"WliHeader" ,
    #"Create a header for wli" )




templates[ "SuperTollSource" ] = basic_source_template(
    "SuperTollSource" ,
    "Creates a source file for SuperToll." ,
    [ "SuperToll" ] , license = copyright_notes.no_copyright_for_header )
templates[ "AModSource" ] = basic_source_template(
    "AModSource" ,
    "Creates a source file for AMod." ,
    [ "AMod" ] , license = copyright_notes.no_copyright_for_header )
templates[ "ZESource" ] = basic_source_template(
    "ZESource" ,
    "Creates a source file for ZE." ,
    [ "ZE" ] , license = copyright_notes.no_copyright_for_header )
templates[ "SimpleSource" ] = basic_source_template(
    "SimpleSource" ,
    "Creates a simple source file." ,
    [ "src" ] , license = copyright_notes.no_copyright_for_header )
#templates[ "WliSource" ] = wli_source_template(
    #"WliSource" ,
    #"Create a source file for wli." )
templates[ "GPCXXExample" ] = basic_source_template(
    "GPCXXExample" ,
    "Create a sample gpcxx application." )
templates[ "FormulaSource" ] = basic_source_template(
    "FormulaSource" ,
    "Creates a simple source file for formula." ,
    [ "formula" ] , license = copyright_notes.no_copyright_for_header )






templates[ "AmbossMain" ] = basic_main_template(
    "AmbossMain" ,
    "Creates a simple main file for Amboss" )
templates[ "SimpleMain" ] = basic_main_template(
    "SimpleMain" ,
    "Creates a simple cpp file with a main function." , [] , copyright_notes.no_copyright_for_header )




templates[ "SuperTollGTest" ] = basic_gtest_template(
    "SuperTollGTest" ,
    "Creates a unit test file for gpcxx." , [ "UnitTest" ] , license = copyright_notes.no_copyright_for_header )
templates[ "GPCXXTest" ] = basic_gtest_template(
    "GPCXXTest" ,
    "Creates a unit test file for gpcxx." , [ "test" ] )
templates[ "AmbossTest" ] = basic_gtest_template(
    "AmbossTest" ,
    "Creates a unit test file for Amboss." , [ "test" ] )
#templates[ "NumdiffTest" ] = basic_gtest_template(
    #"NumdiffTest" ,
    #"Create a unit test file for Numdiff." , [ "test" ] )
templates[ "FormulaTest" ] = basic_gtest_template(
    "FormulaTest" ,
    "Creates a unit test file for Amboss." , [ "test" ] , copyright_notes.no_copyright_for_header )


templates[ "SimpleCMake" ] = basic_cmake_template(
    "SimpleCMake" ,
    "SimpleCMakeLists.txt" )
templates[ "SimpleJamfile" ] = basic_jamfile_template(
    "SimpleJamfile" ,
    "Jamroot" )
templates[ "SimpleMakefile" ] = basic_makefile_template(
    "SimpleMakefile" ,
    "Makefile" )

templates[ "OdeintHeader" ] = odeint_header_template()
templates[ "OdeintMain" ] = odeint_main_template()
templates[ "OdeintTest" ] = odeint_test_template()

templates[ "SuperTollTest" ] = supertoll_test_template()

templates[ "SimpleCppProject" ] = simple_cpp_project_template()
templates[ "CppProject" ] = cpp_project_template()

templates[ "PythonApplication" ] = python_application_template(
    "PythonApplication" ,
    "Creates a python application" )
templates[ "PythonLib" ] = python_lib_template(
    "PythonLib" ,
    "Creates a python library" )
templates [ "SuperTollPythonApplication" ] = supertoll_python_application_template(
    "SuperTollPythonApplication" ,
    "Create a supertoll python application" )


def main():

    parser = argparse.ArgumentParser( description = description )
    subparsers = parser.add_subparsers( help = "subcommand help" )
    ordered_templates = collections.OrderedDict( sorted( templates.items() ) )    
    for name, t in ordered_templates.items() :
        t.register_in_arg_parser( subparsers )

    # parse arguments and evaluate the current template
    argcomplete.autocomplete( parser )
    args = parser.parse_args()
    template = templates[ args.which ]
    template.do_work( args , default_replacements )

    

if __name__ == "__main__" :

    main()
