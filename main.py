from pyeda.inter import *
from helper import *
from math import *
#-----------SHANNON--------------
n = 3
X = exprvars('x', n)
m = ''
g = expr('(x[0]&(x[1]|x[2]))')
g_bar = ~g
 # what comes are maxterms
M=[]
shannon(g_bar,X,0,n,m,M)
minterms = [int(x,2) for x in M]
print("___________SHANNON__________")
print("G : ",g)
print("Minterms : ",minterms)

m = minterms
#--------------McClusky---------------
m = list(set(m))
Nbits = ceil(log(max(m)+1,2))
print("_____________McClusky__________")
print("Minterm Input : ",m)
print("Nbits : ",Nbits)
onMinterm  = mintermType(m,Nbits)
P = sort(onMinterm) # arrange according to number of ones
mcTable = [P]
print('P Table Input : ',len(P))
dispP(P)
mergeP(mcTable,0)
#print("Final Table")
#dispT(mcTable)
primes  = getPrimes(mcTable)
print("Prime : #",len(primes))
dispP(primes)

