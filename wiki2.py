#a sorted_x1
#b onewordlinklist
#c linkdict
#d sorted_x
#s splitted
#o order
#e twowordlinklist
#f sorted_xc
#h capitallinklist
#ii doc1lower

import wikipediaapi
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
import operator
import time

def wikipedialink(a,b,c,d,e,f,h,s,o,ii):
    newcount=0
    wiki_wiki = wikipediaapi.Wikipedia('en')
    for i in range(len(a)):
        page_py = wiki_wiki.page(s[o[a[i][0]]])
        if  page_py.exists():
            time.sleep(0.1)
            links=page_py.links
            dummylist=list()
            dummiestlist=list()
            for j in links.keys():
                dummylist.append(j)
            for k in range(len(dummylist)):
                dummylist[k]=dummylist[k].lower()
                if 'article' not in dummylist[k] and 'category' not in dummylist[k] and 'wiki' not in dummylist[k] and 'link' not in dummylist[k] and 'help' not in dummylist[k] and 'cs1' not in dummylist[k]:
                    text=page_py.text
                    text=text.lower()
                    if text.count(dummylist[k])>=2 and ii.count(dummylist[k])>0:
                        dummiestlist.append(dummylist[k])
            for j in range(len(dummiestlist)):
                    if dummiestlist[j] not in c.keys():
                        c[dummiestlist[j]]=newcount
                        newcount+=1
            b[i]=dummiestlist
    for i in range(len(d)):
        dum = s[o[d[i][0][0]]]+ ' ' +s[o[d[i][0][1]]]
        page_py = wiki_wiki.page(dum)
        if  page_py.exists():
            time.sleep(0.1)
            links=page_py.links
            dummylist=list()
            dummiestlist=list()
            for j in links.keys():
                dummylist.append(j)
            for k in range(len(dummylist)):
                dummylist[k]=dummylist[k].lower()
                if 'article' not in dummylist[k] and 'category' not in dummylist[k] and 'wiki' not in dummylist[k] and 'link' not in dummylist[k] and 'help' not in dummylist[k] and 'cs1' not in dummylist[k]:
                    text=page_py.text
                    text=text.lower()
                    if text.count(dummylist[k])>=2 and ii.count(dummylist[k])>0:
                        dummiestlist.append(dummylist[k])
            for j in range(len(dummiestlist)):
                if dummiestlist[j] not in c.keys():
                    c[dummiestlist[j]]=newcount
                    newcount+=1
            e[i]=dummiestlist
    for i in range(len(f)):
        page_py = wiki_wiki.page(s[o[f[i][0]]])
        if  page_py.exists():
            time.sleep(0.1)
            links=page_py.links
            dummylist=list()
            dummiestlist=list()
            for j in links.keys():
                dummylist.append(j)
            for k in range(len(dummylist)):
                dummylist[k]=dummylist[k].lower()
                if 'article' not in dummylist[k] and 'category' not in dummylist[k] and 'wiki' not in dummylist[k] and 'link' not in dummylist[k] and 'help' not in dummylist[k] and 'cs1' not in dummylist[k]:
                    text=page_py.text
                    text=text.lower()
                    if text.count(dummylist[k])>=2 and ii.count(dummylist[k])>0:
                        dummiestlist.append(dummylist[k])
            for j in range(len(dummiestlist)):
                if dummiestlist[j] not in c.keys():
                    c[dummiestlist[j]]=newcount
                    newcount+=1
            h[i]=dummiestlist
    return
