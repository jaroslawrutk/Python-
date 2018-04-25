#!/usr/bin/env python
#encoding: utf-8

import subprocess
import os

zmienna= int(raw_input())
i=0
p=2
czy=1

while(zmienna!=1):
    print("A")
    i=0
    czy=0
    for x in range(2, p):
        print("B")
        if(p%x==0):
            czy=1
            break
        
    if(czy==0):
        while(zmienna%p==0):
            print("C")
            zmienna=zmienna/p
            i=i+1
            
print("("+p+","+str(i)+")")
