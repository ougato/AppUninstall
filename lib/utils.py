# -*- coding: utf-8 -*-

# Author: oucheng(ougato@gmail.com)
# Copyright (c) 2018-09

import os

def isdir( path ):
    return os.path.isdir( path )

def isfile( path ):
    return os.path.isfile( path )

def islink( path ):
    return os.path.islink( path )