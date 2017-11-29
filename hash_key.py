#!/usr/bin/python

import math,string

def split_keys (alphabet, longueur, partition):
    total = int(math.pow (len (alphabet), longueur))
    div = total // partition
    mod = total % partition

    nombres = []
    x = 0
    for i in range (0,partition):
        x = x + div
        if i < mod:
            x = x + 1
        nombres.append(x)
    nombres.pop()
    #print nombres

    res=[]
    for nombre in nombres:
        trans=[]
        a = nombre
        b = len(alphabet)
        while True:
            q = a // b
            r = a % b
            trans.append (r)
            a = q
            if q < b:
                break
        trans.append (q)
        res.append(trans)
    max_div = len (res[-1])
    for xx in res:
        while len(xx) < max_div:
            xx.append(0)
    #print res
    res2 = []
    for i in res:
        res3=[]
        for j in i:
            res3.append(alphabet[j])
        res2.append(res3)
    return res2

def reverse_keys (keys):
    for key in keys:
        key.reverse()

def concat_keys (keys):
    r = []
    for key in keys:
        q = ""
        for x in key:
            q = q + x
        r.append (q)
    return r

#alphabet = ['0','1','2','3','4','5','6','7','8','9']
alphabet = list(string.ascii_letters)
longueur = 10
partition = 10

keys = split_keys (alphabet, longueur, partition)
#print keys
reverse_keys (keys)
#print keys
r = concat_keys (keys)
print r
