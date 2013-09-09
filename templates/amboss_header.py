#! /usr/bin/python

from basic_class_template import basic_class_template
import helpers



class amboss_header():
    
    def __init__( self ) :
        self.template = basic_class_template( "Amboss" , [ "Amboss" ] , [ "Amboss" ] )
        self.name = "AmbossHeader"
        self.description = "Creates a simple header with header guards for Amboss."
        
    def register_in_arg_parser( self , subparsers ):
        self.template.register_in_arg_parser( self , subparsers )
        
    def do_work( self , args , replacements ):
        self.template.do_work( self , args , replacements )
