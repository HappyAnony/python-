#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony


import os
import sys

BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
#print(BASE_DIR)
#print(sys.path)
sys.path.insert(0,BASE_DIR)
#print(sys.path)

from core import main

if __name__ == '__main__':
    main.run()