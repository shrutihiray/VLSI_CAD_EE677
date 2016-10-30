from math import *
import numpy as np
# Ajinkya Gorad (140110033)
# function to check dominance of two binary representations
# as far as the code can only check dominance and generate  binary representations of each minterm
# a minterm syntax is (m,binary_rep,flag)

def checkDominance(a,b):
    if(a==b): return "="
    a_ = [int(x) for x in list(a)]
    b_ = [int(x) for x in list(b)]
    c = [ x*y for x,y in zip(a_,b_)]
    if c==b_ : return ">"
    if c==a_ : return "<"
    return None
def dispP(P):
    for ip in range(0, len(P)):
        print("P(", ip, ")", P[ip])
def dispT(T):
    for it in range(0,len(T)):
        for ip in range(0,len(T[it])):
            print("T(",it,",",ip,")|",T[it][ip])
def ifDifferByOne(m1,m2):
    if(len([(x,y) for x,y in zip(m1[1],m2[1]) if x!=y])==1):
        return True
    return False
def getDifferingIndex(m,mn):
    for i in range(0,len(m[1])):
        if(m[1][i]!=mn[1][i]):
            return i
    return None
def mergeP(table,id):
    print("called MergeP with table:",id)
    #dispT(table)
    P1 = table[id]
    Pnew = []
    found = False
    for ip in range(0,len(P1)-1):
        for m in P1[ip]:
            for mn in P1[ip+1]:
                if(ifDifferByOne(m,mn)):
                    diff = getDifferingIndex(m,mn)
                    if((m[1][diff]!='-')|(mn[1][diff]!='-')):
                        found = True
                        m_new =list(m)
                        m_new[0] = list(m[0])+list(mn[0])
                        m_new[0] = list(set(m_new[0]))
                        m_new[1] = m_new[1][0:diff]+'-'+m_new[1][diff+1:]
                        m_new[2] = 'Y' # a newly generated term always as 'Y'
                        m[2]='N'        # check them as 'N' as they are included at least once
                        mn[2]='N'
                        if m_new not in Pnew:   # add only if it doesn't exist
                            Pnew.append(m_new)
                        #print(m,"+",mn,"=",m_new)
    Pnew = sort(Pnew)
    table.append(Pnew)
    if(found):
        mergeP(table,id+1)
    return
def getPrimes(table):
    primes = []
    for col in table:
        for minterms in col:
            for minterm in minterms:
                if(minterm[2]=='Y'):
                    minterm[0].sort()
                    primes.append(minterm)
    return sortSet(primes)
# return the minterms haveing number of ones
def getMinterms(minterms,NumOne):
    mi = []
    for m in minterms:
        if(m[1].count('1')==NumOne):
            mi.append(m)
    return mi
def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item
def sortSet(l):
    return list(uniq(sorted(l, reverse=True)))
def sort(minterms):
    P=[]
    NumOne = 0;
    while(len(minterms)):
        mi = getMinterms(minterms,NumOne)
        #print('mi : ',mi)
        P.append(mi)
        minterms = [m for m in minterms if m not in mi] # remove sorted entries
        #print("minterms:",len(minterms),"|",minterms)
        NumOne = NumOne+1
    return P

m = [10,16,44,22,12,14,56,35,36,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,69,6,5,6,59,89,5,52,512]
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
print("Primes(",len(primes),")")
dispP(primes)
#now find the minimum set of Ps from them such that all numbers are covered
