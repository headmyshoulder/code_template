#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import argparse
import argcomplete
import datetime
import os
import glob

from yapsy.PluginManager import PluginManager

from templates.amboss_header import *
from templates.gpcxx_header import *


description = "Create source code templates for commonly used files."

directories = [ os.path.join( os.path.dirname( os.path.realpath(__file__) ) , "templates" ) ]

config = {
    "Author" : "Karsten Ahnert" ,
    "AuthorEmail" : "karsten.ahnert@gmx.de"
}

default_replacements = {
    "AUTHOR" : config[ "Author" ] ,
    "AUTHOREMAIL" : config[ "AuthorEmail" ] ,
    "DATE" : datetime.date.today().isoformat()
}




parser = argparse.ArgumentParser( description = description )

subparsers = parser.add_subparsers( help = "subcommand help" )
templates = {}



def register_plugin( plugin_info ):
    #print plugin_info.name
    #print plugin_info.description
    #print plugin_info.plugin_object
    #print

    plugin = plugin_info.plugin_object
    plugin.set_name( plugin_info.name )
    plugin.set_description( plugin_info.description )
    plugin.register_in_arg_parser( subparsers )
    templates[ plugin.name ] = plugin

def plugin_sort( p1 , p2 ):
    if( p1.name < p2.name ) : return -1
    else :
        if( p1.name == p2.name ) : return 0
        else : return 1

templates[ "AmbossHeader" ] = amboss_header()
templates[ "GPCXXHeader" ] = gpcxx_header()

def main():
    
    # Load and register all plugins
    #manager = PluginManager( directories_list = directories )
    #manager.collectPlugins()
    #plugins = manager.getAllPlugins()
    #plugins.sort( plugin_sort )
    #for plugin in plugins:
        #register_plugin( plugin ) 
    
    for name, t in templates.items() :
        t.register_in_arg_parser( subparsers )

    # parse arguments and evaluate the current template
    argcomplete.autocomplete( parser )
    args = parser.parse_args()
    template = templates[ args.which ]
    template.do_work( args , default_replacements )

    

if __name__ == "__main__" :

    main()
