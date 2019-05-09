# -*- coding: utf-8 -*-

# Author: oucheng(ougato@gmail.com)
# Copyright (c) 2018-09

import os
import json
import platform
import sys

lib = os.path.dirname( os.path.dirname( os.path.abspath( sys.argv[0] ) ) ) + "/" + "lib"
src = os.path.dirname( os.path.dirname( os.path.abspath( sys.argv[0] ) ) ) + "/" + "src"
conf = os.path.dirname( os.path.dirname( os.path.abspath( sys.argv[0] ) ) ) + "/" + "conf"
sys.path.append( lib )
sys.path.append( src )
sys.path.append( conf )

import utils

COMMAND_PATH = "./conf/command.json"

def change_dir( exec_file ):
    os.chdir( os.path.dirname( os.path.dirname( os.path.abspath( exec_file ) ) ) )
    os.system( "pwd" )

def read_json( app_name ):
    platform_sys = platform.system()
    command_fd = open( COMMAND_PATH, "r", encoding="utf-8", )
    print( json.loads( command_fd.read() ) )
    print( sys.argv[1] )
    print( json.loads( command_fd.read() ) )
#     return json.loads( command_fd.read() )[app_name][platform_sys]

def clean_app( commands ):
    for command in commands:
        os.system( command )

def main():
    argv0, argv1 = sys.argv[0], sys.argv[1]
    change_dir( argv0 )
    read_json( argv1 )
#     clean_app( read_json( argv1 ) )

if __name__ == "__main__":
    main()
