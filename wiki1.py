#aa noofwords
#b Sorted_x1
#c onewordcategorylist
#d categorydict
#s splitted
#e Sorted_xc
#f capitalcategorylist
#g Sorted_x
#h twowordcategorylist

import numpy
import operator
import time

def matrixcreation(aa,b,c,d,s,e,f,g,h):
    categorywordmatrix=numpy.zeros(shape=(len(aa),len(d.values())))
    categorylist = list(d.values())
    for i in range(len(aa)):
        if aa[i] in b:
            ourno = b.index(aa[i])
            try:
                for k in range(len(c[ourno])):
                    if s(aa[i]) in c[ourno][k]:
                        a= d[c[ourno][k]]
                        a = categorylist.index(a)
                        categorywordmatrix[i][a]+=1
            except:
                None
            try:
                for k in range(len(c[ourno])):
                    a= d[c[ourno][k]]
                    a = categorylist.index(a)
                    categorywordmatrix[i][a]+=1

            except:
                continue
    for i in range(len(aa)):
        if aa[i] in e:
            ourno = e.index(aa[i])
            try:
                for k in range(len(f[ourno])):
                    if s(aa[i]) in f[ourno][k]:
                        a= d[f[ourno][k]]
                        a = categorylist.index(a)
                        categorywordmatrix[i][a]+=1
            except:
                None
            try:
                for k in range(len(f[ourno])):
                    a= d[f[ourno][k]]
                    a = categorylist.index(a)
                    categorywordmatrix[i][a]+=1
            except:
                continue
    for i in range(len(aa)):
        if aa[i] in g:
            ourno = g.index(aa[i])
            try:
                for k in range(len(h[ourno])):
                    if (s(aa[i][0])+' '+ s(aa[i][1])) in h[ourno][k]:
                        a= d[h[ourno][k]]
                        a = categorylist.index(a)
                        categorywordmatrix[i][a]+=1
            except:
                None
            try:
                for k in range(len(h[ourno])):
                    a= d[h[ourno][k]]
                    a = categorylist.index(a)
                    categorywordmatrix[i][a]+=1
            except:
                continue
    return categorywordmatrix
