from pyeda.inter import *
zero = expr(0)
one = expr(1)
#-------------DEFINATIONS------------
def displayPrimeImplicantTable(m,P):
    if(len(P)==0):
        print("EMPTY TABLE")
        return
    line ="____"
    fStr = '{0:03d}'
    for k in range(0,len(P)):
        line =line+ "\t|"+P[k][1]+"|"
    print(line)
    line = "<<<<"
    for k in range(0,len(P)):
        line = line+"\t"+str(P[k][0])
    line = line+">>>>>"
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
def getm(S):
    return [s[0] for s in S]
def removeDominatingRow(m,P):
    S = getS(m,P)
    print("Sr")
    dispP(S)
    for s in S:
        for s2 in S:
            if(s!=s2):
                if(set(s[1])>set(s2[1])):
                    if(s in S):
                        S.remove(s)
    P = getP(S)
    m = getm(S)
    return m,P
def removeDominatedCol(m,P):
    dispP(P)
    for p in P:
        for p2 in P:
            if (p != p2):
                if (set(p[0]) >= set(p2[0])):
                    P.remove(p)
    return m,P


def tableReduce(m,P):
    S = getS(m, P) # S gets modified in loop
    essentialPrimes = []
    iter = 0
    print("Prime Implicant Table")
    displayPrimeImplicantTable(m,P)
    while(len(P)!=0):
        iter = iter+1
        print("[ITERATION TABLE REDUCE : ",iter,"]")
        print(S)
        for s in S:
            if(len(s[1])==1):
                essentialPrimes.append(s)
                if(s[0] in m):
                    m.remove(s[0])
        sTrash=[s for s in S for ep in essentialPrimes if ep[1][0] in s[1] ] # remove the minterm common primes
        # remove minterms corresponding to particular
        S = [s for s in S if s not in sTrash]
        P = getP(S)
        m = getm(S)
        print("Removed essential Prime Implicants")
        displayPrimeImplicantTable(m,P)
        m,P=removeDominatingRow(m,P)
        print("Removed Dominating Rows in Prime Implicant Table")
        displayPrimeImplicantTable(m,P)
        m,P=removeDominatedCol(m,P)
        print("Removed Dominated Columns")
        displayPrimeImplicantTable(m,P)
        S = getS(m,P)
    ep = [e[1][0] for e in essentialPrimes]
    return ep
def primesOfminterm(m,primes):
    S = []
    for mi in m:
        S.append([minterm[1] for minterm in primes if mi in minterm[0]])
    return S
def mintermsOfprime(S):
    m = [ s[0] for s in S ]
    primes = []
    for s in S:
        for p in s[1]:
            if(p not in primes):
                primes.append(p)
    P =[]
    for p in primes:
        P.append( [[s[0] for s in S if p in s[1]],p,'R'] )
    return P
# renamed from mintermType  to mineterm2BinString
def minterm2BinString(m,Nbits):
    formatString = '{0:0' + str(Nbits) + 'b}'
    onMinterm = []
    for minterm in m:
        bin = formatString.format(minterm)
        onMinterm.append([[minterm], bin, 'Y'])  # mark all tags as yes initially
    return onMinterm
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
def dispX(X,L,title):
    print("-----",title,"-----")
    for ip in range(0, len(X)):
        print(L,"(", ip, ")", X[ip])
def ifDifferByOne(m1,m2):
    if(len([(x,y) for x,y in zip(m1[1],m2[1]) if x!=y])==1):
        return True
    return False
def getDifferingIndex(m,mn):
    for i in range(0,len(m[1])):
        if(m[1][i]!=mn[1][i]):
            return i
    return None
def mergeTable(table,id):
    print("called MergeTable with table:",id)
    dispT(table)
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
    Pnew = sortNumOne(Pnew)
    table.append(Pnew)
    if(found):
        mergeTable(table,id+1) # use recursion
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
def sortNumOne(minterms):
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

def shannon(f,X,i,n,m,M):
    if(i == n):
        return
    f1_bar = f.restrict({X[i]: zero})
    f1 = f.restrict({X[i]: one})

    if(i == n-1):
        if(f1 == one):
            M.append('1'+m)
        if(f1_bar == one):
            M.append('0'+m)

    print("SH: <",i,'> f1 : ',f1,'f1_bar : ',f1_bar)
    shannon(f1_bar,X,i+1,n,'0'+m,M)
    shannon(f1,X,i+1,n,'1'+m,M)
    return
# To Convert the essential primes to string equivalent
def prime2Str(p):
    out = []
    for prime in p:
        n = len(prime)
        primeStr=''
        for i in range(0,n):
            if(prime[i]=='1'):
                primeStr = 'x'+str(i)+'+'+primeStr
            if(prime[i]=='0'):
                primeStr = '~x'+str(i)+'+'+primeStr
        primeStr = primeStr[:-1]
        out.append(primeStr)
    return out

