#a sorted_x1
#b onewordcategorylist
#c categorydict
#d sorted_x
#s splitted
#o order
#e twowordcategorylist
#f sorted_xc
#h capitalcategorylist

import wikipediaapi
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
import operator
import time

def wikipediacategory(a,b,c,d,e,f,h,s,o):
    count=0
    wiki_wiki = wikipediaapi.Wikipedia('en')
    for i in range(len(a)):
        page_py = wiki_wiki.page(s[o[a[i][0]]])
        if  page_py.exists():
            time.sleep(0.1)
            categories=page_py.categories
            dummylist=list()
            dummiestlist=list()
            for j in categories.keys():
                dummylist.append(j)
            for k in range(len(dummylist)):
                dummylist[k]=dummylist[k].lstrip("Category")
                dummylist[k]= dummylist[k].lstrip(":")
                dummylist[k]=dummylist[k].lower()
                if 'disambiguation' in dummylist[k]:
                #Burada link ile disambiguationu cozecegiz
                    links=page_py.links
                    dummy=list()
                    for w in links.keys():
                        dummy.append(w)
                    for u in range(len(dummy)):
                        dummy[u]=dummy[u].lower()
                        if 'talk' not in dummy[u] and 'help' not in dummy[u]:
                            dummiestlist.append(dummy[u])
                    break
                if 'republics' not in dummylist[k] and 'nations' not in dummylist[k] and 'dispute' not in dummylist[k] and 'subscription' not in dummylist[k] and 'use' not in dummylist[k] and 'vague or ambiguous' not in dummylist[k] and 'article' not in dummylist[k] and 'page' not in dummylist[k] and 'wiki' not in dummylist[k] and 'link' not in dummylist[k] and 'source' not in dummylist[k] and 'cs1' not in dummylist[k]:
                    dummiestlist.append(dummylist[k])
            for j in range(len(dummiestlist)):
                    if dummiestlist[j] not in c.keys():
                        c[dummiestlist[j]]=count
                        count+=1
            b[i]=dummiestlist
    for i in range(len(d)):
        dum = s[o[d[i][0][0]]]+ ' ' +s[o[d[i][0][1]]]
        page_py = wiki_wiki.page(dum)
        if  page_py.exists():
            time.sleep(0.1)
            categories=page_py.categories
            dummylist=list()
            dummiestlist=list()
            for j in categories.keys():
                dummylist.append(j)
            for k in range(len(dummylist)):
                dummylist[k]=dummylist[k].lstrip("Category")
                dummylist[k]= dummylist[k].lstrip(":")
                dummylist[k]=dummylist[k].lower()
                if 'republics' not in dummylist[k] and 'nations' not in dummylist[k] and 'dispute' not in dummylist[k] and 'subscription' not in dummylist[k] and 'use' not in dummylist[k] and 'vague or ambiguous' not in dummylist[k] and 'article' not in dummylist[k] and 'page' not in dummylist[k] and 'wiki' not in dummylist[k] and 'link' not in dummylist[k] and 'source' not in dummylist[k] and 'cs1' not in dummylist[k]:
                    dummiestlist.append(dummylist[k])
            for j in range(len(dummiestlist)):
                if dummiestlist[j] not in c.keys():
                    c[dummiestlist[j]]=count
                    count+=1
            e[i]=dummiestlist
    for i in range(len(f)):
        page_py = wiki_wiki.page(s[o[f[i][0]]])
        if  page_py.exists():
            time.sleep(0.1)
            categories=page_py.categories
            dummylist=list()
            dummiestlist=list()
            for j in categories.keys():
                dummylist.append(j)
            for k in range(len(dummylist)):
                dummylist[k]=dummylist[k].lstrip("Category")
                dummylist[k]= dummylist[k].lstrip(":")
                dummylist[k]=dummylist[k].lower()
                if 'republics' not in dummylist[k] and 'nations' not in dummylist[k] and 'dispute' not in dummylist[k] and 'subscription' not in dummylist[k] and 'use' not in dummylist[k] and 'vague or ambiguous' not in dummylist[k] and 'article' not in dummylist[k] and 'page' not in dummylist[k] and 'wiki' not in dummylist[k] and 'link' not in dummylist[k] and 'source' not in dummylist[k] and 'cs1' not in dummylist[k]:
                    dummiestlist.append(dummylist[k])
            for j in range(len(dummiestlist)):
                if dummiestlist[j] not in c.keys():
                    c[dummiestlist[j]]=count
                    count+=1
            h[i]=dummiestlist
    return
