#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

import os
import sys

print(__file__)
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
print(BASE_DIR)
sys.path.append(BASE_DIR)

from core import main
from conf import settings

main.test()