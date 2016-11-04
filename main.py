from pyeda.inter import *
from helper import *
from math import *
def displayPrimeImplicantTable(m,P):
    line ="____"
    fStr = '{0:03d}'
    for k in range(0,len(P)):
        line =line+ "\t|"+P[k][1]+"|"
    print(line)
    line = ''
    for k in range(0,len(P)):
        line = line+"\t"+str(P[k][0])
    print(line)
    for y in range(0,len(m)):
        line = "[" + fStr.format(m[y]) + "]"
        for x in range(0,len(P)):
            line = line+"\t\t"
            if(m[y] in P[x][0]):
                line = line+"X"
            else:
                line = line+"-"
        print(line)
def getS(m,P):
    return list(zip(m, primesOfminterm(m, P)))
def getP(S):
    return mintermsOfprime(S)
def removeDominatingRow(m,P):
    return
def tableReduce(m,P):
    S = getS(m, P) # S gets modified in loop
    #while(len(P)!=0):
    print(S)
    essentialPrimes = [ ]
    for s in S:
        if(len(s[1])==1):
            essentialPrimes.append(s)
            if(s[0] in m):
                m.remove(s[0])


    print("m,Essential Primes: ", essentialPrimes)
    P = [ p for p in P if p[1] not in [e[1][0] for e in essentialPrimes]]
    sTrash=[s for s in S for ep in essentialPrimes if ep[1][0] in s[1] ] # remove the minterm common primes
    # remove minterms corresponding to particular
    S = [s for s in S if s not in sTrash]
    m = [s[0] for s in S]
    displayPrimeImplicantTable(m,P)
    print(" S :")
    dispP(S)
    print(" P :")
    dispP(P)
    mintermsOfprime(S)
#-----------SHANNON--------------
n =5
X = exprvars('x', n)
m = ''
g = expr('(x[0]&(x[1]|x[2]))^x[3]|(x[4]&x[1]|x[2])')
g_bar = ~g
 # what comes are maxterms
M=[]
shannon(g_bar,X,0,n,m,M)
minterms = [int(x,2) for x in M]
print("___________SHANNON__________")
print("G : ",g)
print("Minterms : ",minterms)

#m = minterms
m = [0,2,5,6,7,8,10,12,13,14,15   ]
#--------------McClusky---------------
m = list(set(m))
Nbits = ceil(log(max(m)+1,2))
print("_____________McClusky__________")
print("Minterm Input : ",m)
print("Nbits : ",Nbits)
onMinterm  = mintermType(m,Nbits)
P = sortNumOne(onMinterm) # arrange according to number of ones
mcTable = [P]
print('P Table Input : ',len(P))
dispP(P)
mergeP(mcTable,0)
#print("Final Table")
#dispT(mcTable)
primes  = getPrimes(mcTable)
print("Prime(P) : #",len(primes))
dispP(primes)

S = primesOfminterm(m,primes)
print("Minterms and their Primes(S):")
dispP(list(zip(m,S)))

# GOAL : FIND ESSENTIAL PRIME IMPLICANTS
print( "________PRIME IMPLICANT TABLE_________")
displayPrimeImplicantTable(m,primes)
tableReduce(m,primes)