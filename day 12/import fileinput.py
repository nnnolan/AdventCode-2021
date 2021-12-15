from functools import*
N,s,E={},'start',frozenset()
for l in open('input.txt'):
 p=l.strip().split('-')
 for i in(0,1):N[p[i]]=N.get(p[i],E)|{p[~i]}
c=lru_cache()(lambda v,S,f:sum((c(w,(S,S|{v})[v[0]>='a'],f|(w in S)),1)[w=='end']for w in N[v]-({s},S)[f])) 
print(c(s,E,1),c(s,E,0))