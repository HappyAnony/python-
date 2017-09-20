#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony


import os
import sys

BASE_PATH =os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
# print(BASE_PATH)
sys.path.append(BASE_PATH)
# print(sys.path)

from core import main

if __name__ == '__main__':
    main.run()