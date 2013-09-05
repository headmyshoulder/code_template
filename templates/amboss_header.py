#! /usr/bin/python

from basic_class_template import basic_class_template
import helpers



class amboss_header( helpers.APlugin ):
    
    def __init__( self ) :
        self.template = basic_class_template( "AMBOSS" )
        
    def register_in_arg_parser( self , subparsers ):
        self.template.register_in_arg_parser( self , subparsers )
        
    def do_work( self , args , replacements ):
        self.template.do_work( self , args , replacements )
