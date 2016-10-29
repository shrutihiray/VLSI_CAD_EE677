from math import *
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
def ifDifferByOne(m1,m2):
    if(len([(x,y) for x,y in zip(m1[1],m2[1]) if x!=y])==1):
        return True
    return False
# return the minterms haveing number of ones
def getMinterms(minterms,NumOne):
    mi = []
    for m in minterms:
        if(m[1].count('1')==NumOne):
            mi.append(m)
    return mi
def divideMinterms(minterms):
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
m = [1,2,3,4,5,8,9,10]
Nbits = ceil(log(max(m),2))
formatString = '{0:0'+str(Nbits)+'b}'
onMinterm = []
for minterm in m:
    bin = formatString.format(minterm)
    onMinterm.append([minterm,bin,'Y']) # mark all tags as yes initially
print(onMinterm)
P = divideMinterms(onMinterm)
print('P : ',len(P),'|',P)
for m1 in onMinterm:
    for m2 in onMinterm:
        print(m1,"|",m2,":",ifDifferByOne(m1,m2))
# Now Sort the Level 0