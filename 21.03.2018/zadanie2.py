#!/usr/bin/env python
#encoding: utf-8
import sys

with open(sys.argv[1],"r") as f:
    napis1=f.read()
    

def funkcja(napis):
    
    slownik={}
    
    napis2=str(napis).splitlines()
    
    for i in filter(None,napis2):
        slownik2=str(i).split(":")
        slownik[slownik2[0]]=slownik2[1]

    return slownik


print funkcja(napis1)


