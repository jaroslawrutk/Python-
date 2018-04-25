#!/usr/bin/env python
#encoding: utf-8

import subprocess
import os

try:
    out2=subprocess.check_output(["g++ -o programik programik.cpp"], shell=True)
    
except subprocess.CalledProcessError as ex:
print("Program sie nie kompiluje")
