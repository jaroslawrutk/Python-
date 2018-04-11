#!/usr/bin/env python
#encoding: utf-8

import urllib2

a=urllib2.urlopen('http://wykop.pl/')
htmlik=response.read()

f=open("pliczekhtml.html","w")
f.write(htmlik)
f.close()
