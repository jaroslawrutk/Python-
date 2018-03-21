#!/usr/bin/env python
#encoding: utf-8
import sys

with open(sys.argv[1],"r") as f:
    napis1=f.read()
    

def funkcja(napis):
    
    slownik={}
    
    for linia in napis:
        for slowo in linia.split():
            if(slowo in slownik):
                slownik[slowo]+=1
            else:
                slownik[slowo]=1

    return slownik


print funkcja(napis1)


