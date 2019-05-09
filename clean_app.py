# -*- coding: utf-8 -*-

# Author: oucheng(ougato@gmail.com)
# Copyright (c) 2018-09

import os
import json
import platform
import sys

from lib import utils

COMMAND_PATH = "./conf/command.json"

def change_dir( exec_file ):
    os.chdir( os.path.dirname( os.path.dirname( os.path.abspath( exec_file ) ) ) )

def read_json( app_name ):
    platform_sys = platform.system()
    command_fd = open( COMMAND_PATH, "r", encoding="utf-8", )
    return json.loads( command_fd.read() )[app_name][platform_sys]

def clean_app( commands ):
    for command in commands:
        print( command )
        os.system( command )

def main():
    argv0, argv1 = sys.argv[0], sys.argv[1]
    change_dir( argv0 )
    clean_app( read_json( argv1 ) )

if __name__ == "__main__":
    main()
