from math import sqrt
import os
a="Ala ma kota"
lista=[(slowo,len(slowo)) for slowo in a.split()]
print (lista)

a=1
liczba=1

#n=input();
zlotypodzial= (1+5**0.5)/2

#fib=[ int( ((zlotypodzial)**i - (1- zlotypodzial)**i) / (5**(0.5))) for i in range(0,n) ]
#print (fib)

def funklog(a):
    return (a > 0)

lista1=[]

def funkcja(funklog, liczba):
    if (funklog(liczba)):
        lista1.append(liczba)

funkcja(funklog,7)
funkcja(funklog,8)
funkcja(funklog,3)
funkcja(funklog,19)
print (lista1)
punkt_kontrolny=(14,8)
lista_punkt=[(1,4),(3,2),(5,8),(2,4),(7,3)]

odleglosc=[]

def punkty(lista_punkt,punkt_kontrolny):
    for i in range(len(lista_punkt)):
      odleglosc.append((sqrt( (punkt_kontrolny[0]-lista_punkt[i][0])**2 +(punkt_kontrolny[1]-lista_punkt[i][1])**2),lista_punkt[i]))
      
    
punkty(lista_punkt,punkt_kontrolny)    

krotka=sorted(odleglosc,key=lambda tup: tup[0])    
    
print (krotka)

path="C:\\Users\Student.DESKTOP-ICOM-TR\Desktop"

for plik2 in os.listdir(path):
    print (plik2)




