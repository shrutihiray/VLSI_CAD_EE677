<<<<<<< HEAD
from math import *
# Ajinkya Gorad (140110033)
# function to check dominance of two binary representations
# as far as the code can only check dominance and generate  binary representations of each minterm
def checkDominance(a,b):
    if(a==b): return a+"Equal"+b
    a_ = [int(x) for x in list(a)]
    b_ = [int(x) for x in list(b)]

    c = [ x*y for x,y in zip(a_,b_)]
    if c==b_ : return a+ " dominates "+b
    if c==a_ : return b+" dominates "+a
    return b+" Independent "+a

m = [1,2,3,4,5,8,9,10]
Nbits = ceil(log(max(m),2))
formatString = '{0:0'+str(Nbits)+'b}'
onMinterm = []
for minterm in m:
    bin = formatString.format(minterm)
    onMinterm.append([minterm,bin,'Y']) # mark all tags as yes initially
print(onMinterm)

for i in onMinterm:
    for j in onMinterm:
        if(not(i==j)):
            print(checkDominance(i[1],j[1]))

=======
from math import *
# Ajinkya Gorad (140110033)
# function to check dominance of two binary representations
# as far as the code can only check dominance and generate  binary representations of each minterm
def checkDominance(a,b):
    if(a==b): return a+"Equal"+b
    a_ = [int(x) for x in list(a)]
    b_ = [int(x) for x in list(b)]

    c = [ x*y for x,y in zip(a_,b_)]
    if c==b_ : return a+ " dominates "+b
    if c==a_ : return b+" dominates "+a
    return b+" Independent "+a

m = [1,2,3,4,5,8,9,10]
Nbits = ceil(log(max(m),2))
formatString = '{0:0'+str(Nbits)+'b}'
onMinterm = []
for minterm in m:
    bin = formatString.format(minterm)
    onMinterm.append([minterm,bin,'Y']) # mark all tags as yes initially
print(onMinterm)

for i in onMinterm:
    for j in onMinterm:
        if(not(i==j)):
            print(checkDominance(i[1],j[1]))

>>>>>>> 3b588b64fa01fb9b4265d799acf6a614d0d086ad
# Now Sort the Level 0