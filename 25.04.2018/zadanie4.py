#!/usr/bin/env python
#encoding: utf-8

from math import *
 
def rozklad(x):
    if x<=0:
        return 0
    i=2
    ile=0
    r=[] #używana jest tablica (lista), nie bepośrednie wypisywanie
    while x>1:
        
        if x%i==0:
            ile=ile+1
            x/=i
            if(x==1):
                r.append((i,ile))
        else:
            if(ile>0):
                r.append((i,ile))
            i=i+1
            ile=0
    return r
    
 
l=1
print("Podaj liczbę: ")
l=int(input())
r=rozklad(l)
print(r)
    
