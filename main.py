from pyeda.inter import *
from helper import *
from math import *
#-----------SHANNON--------------
n = 3
X = exprvars('x', n)
m = ''
g = expr('(x[0]&(x[1]|x[2]))')
g = ~g
 # what comes are maxterms
M=[]
shannon(g,X,0,n,m,M)
print("MINTERM: ",M)
Maxterms = [int(x,2) for x in M]
print(Maxterms)

m = Maxterms
#--------------McClusky---------------
m = list(set(m))
Nbits = ceil(log(max(m)+1,2))
print("Nbits : ",Nbits)
formatString = '{0:0'+str(Nbits)+'b}'
onMinterm = []
for minterm in m:
    bin = formatString.format(minterm)
    onMinterm.append([[minterm],bin,'Y']) # mark all tags as yes initially
print(onMinterm)
P = sort(onMinterm) # arrange according to number of ones
mcTable = [P]
print('P : ',len(P),'|',P)

mergeP(mcTable,0)
#print("Final Table")
#dispT(mcTable)
primes  = getPrimes(mcTable)
print("Primes(",len(primes),")",primes)
dispP(primes)
#now find the minimum set of Ps from them such that all numbers are covered
S = []
for mi in m:
    S.append([minterm[1] for minterm in primes if mi in minterm[0]])
print('S-----------')
dispP(S)
