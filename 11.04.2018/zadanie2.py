#!/usr/bin/env python
#encoding: utf-8

import re

class sprawdzamMail(Exception):
	adres=[]
	def __init__(self, a):
		if not re.match('(<)?(\w+@\w+(?:\.\w+)+)(?(1)>)', a):
			raise MailException("zły e-mail")
		else:
			self.adres.append(a)

def sprawdz(a):
    try:
        m=sprawdzamMail(a)
    except(MailException)
        print("zły e-mail")
    else:
        print(m)

sprawdz("ala@kot.com")
