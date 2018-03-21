#!/usr/bin/env python
#encoding: utf-8

def funkcja(napis):
    
    slownik={}
    
    napis2=str(napis).splitlines()
    
    for i in napis2:
        slownik2=str(i).split(":")
        slownik[slownik2[0]]=slownik2[1]

    return slownik


print funkcja("'k1:w1 \n k2:w2 \n k3:w3'")


