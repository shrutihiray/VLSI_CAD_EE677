from pyeda.inter import *
from helper import *
from math import *
def McClusky(m,Nbits):

    print("__________________Mc CLUSKY_____________________")
    print("MINTERM INPUT  (BITS :",Nbits,"): ",m)
    mintermBinary = minterm2BinString(m,Nbits) # convert minterms into their binary strings
    P = sortNumOne(mintermBinary)              # create the table P with minterm ( STORE PRIME TO MINTERM MAPPING)
    dispX(P,"M","MintermBinaryTable")
    McTable = [P]
    mergeTable(McTable,0)       # merge and find all possible minterms
    dispX(McTable,"McT","Mc Table Merged")
    primes = getPrimes(McTable)    # get the primes from the table ( values marked as Y)
    dispX(primes,"Pr","Prime Implicants")
    S = getS(m,primes) # sort the inverse of STORE MINTERM TO PRIME MAPPING
    dispX(S,"S","MINTERM TO PRIME MAPPING (INPUT)")
    print("________PRIME IMPLICANT TABLE_________")
    displayPrimeImplicantTable(m, primes)
    essentialPrimes = tableReduce(m, primes)
    print("Essential Prime Implicants :",essentialPrimes)
    return essentialPrimes
def getEssentialImplicants(f,X):
    f_bar = f # complement the function to get the minterms
    n = len(X)  # number of variables
    # SHANNON METHOD FOR FINDING MINTERMS
    m=''
    M =[]
    shannon(f_bar,X,0,n,m,M)
    minterms = [ int(x,2) for x in M]
    print("______________SHANNON EXPANSION_______________")
    print("Expression :",f)
    print("Minterms :",minterms)
    m = minterms
    # MCCLUSKY ALGORITHM FOR REDUCING ON MINTERMS AND FINDING PRIME IMPLICANTS  TO ESSENTIAL PRIME  IMPLICANTS
    m = list(set(m))     # make sure all minterms are unique
    Nbits = ceil(log(max(m)+1,2)) # Get number of Bits to work with
    essentialPrimes = McClusky(m,Nbits) # call McCluksy Function for  getting essential prime implicants
    return essentialPrimes
# To Convert the essential primes to string equivalent
def prime2Str(p):
    SOP = []
    for prime in p:
        n = len(prime)
        primeStr=''
        for i in range(0,n):
            if(prime[i]=='1'):
                primeStr = 'x'+str(i)+'.'+primeStr
            if(prime[i]=='0'):
                primeStr = '~x'+str(i)+'.'+primeStr
        primeStr = primeStr[:-1]
        SOP.append(primeStr)
    return SOP

#-----------SHANNON--------------
n =4
X = exprvars('x', n)

f = expr('(x[1]^x[0])^(x[2]&x[3])')
ep = getEssentialImplicants(f,X)
print("+=========+")
print(prime2Str(ep))