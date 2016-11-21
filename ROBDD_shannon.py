from pyeda.inter import * 

#AUTHOR: SHRUTI HIRAY, 14d070016
zero = expr(0)
one = expr(1)
f_list = [] #List contains all the prime implicants required for POS form

#Function computes the max terms and minimises it i.e (x0 | x1)(x0 | ~x1) is redundant and can be expressed as (x0). Not necessary upto optimum level

robdd_store = [ ( '0',None,None ), ('1',None,None ) , ('x[0]',0,1) , ('x[0]',1,0), ('x[1]',0,1), ('x[1]',1,0), \
    ('x[2]',0,1), ('x[2]',1,0), ('x[3]',6,7), ('x[3]',7,6), ('x[0]',8,9), ('x[1]',0,6), ('x[0]',0,11), ('x[0]',4,1) ]

print (ITE(robdd_store[13][0],robdd_store[4][0],one))
def compute_robdd_to_f(n):
	E = robdd_store[n][1]
	if(E==0):
		f_E = zero
	elif(E==1):
		f_E = one
	else:
		f_E = compute_robdd_to_f(E)
	T = robdd_store[n][2]
	if(T==0):
		f_T = zero
	elif(T==1):
		f_T = one
	else:
		f_T = compute_robdd_to_f(T)
	#print(E,T,ITE(robdd_store[n][0],f_T,f_E))
	return ITE(robdd_store[n][0],f_T,f_E)

def compute_min_shannon(f,f_list,X,i,n):
	f_E_i = f.restrict({X[i]: zero})
	f_T_i = f.restrict({X[i]: one})
	if(f_E_i == f_T_i):
		if(f_E_i != one): #No need to proceed if value is one
			if(i==n-1):
				f_list.append(f)  #Only leaf nodes are appended
			else:
				compute_min_shannon(f,f_list,X,i+1,n) 
	else:
		if(f_E_i != one ): #No need to proceed if value is one
			f_E = expr(X[i]) | f_E_i
			if(i==n-1):
				
				f_list.append(f_E) #Only leaf nodes are appended
			else:
				compute_min_shannon(f_E,f_list,X,i+1,n)	 
		if(f_T_i != one ): #No need to proceed if value is one
			f_T = expr(~X[i]) | f_T_i
			if(i==n-1):
				
				f_list.append(f_T) #Only leaf nodes are appended
			else:
				compute_min_shannon(f_T,f_list,X,i+1,n)	
	return

def compute_shannon(f,f_list,X,i,n):
	f_E_i = f.restrict({X[i]: zero})
	f_T_i = f.restrict({X[i]: one})
	
	f_E = expr(X[i]) | f_E_i
	if(i==n-1):
		if(f_E_i != one):		
			f_list.append(f_E) #Only leaf nodes are appended
	else:
		compute_shannon(f_E,f_list,X,i+1,n)	 
	
	f_T = expr(~X[i]) | f_T_i
	if(i==n-1):
		if(f_T_i != one):
			f_list.append(f_T) #Only leaf nodes are appended
	else:
		compute_shannon(f_T,f_list,X,i+1,n)	
	return

# Example Case
n=3
X = exprvars('x', n)
g = expr('(x[0]&x[1]&x[2])')
print (g)
f_list = []
h = one
compute_shannon(g,f_list,X,0,n)
for i in f_list:
	h = h & i
print ("f_list",f_list)
#Output is as follows:
#[Or(x[0], 0), Or(x[2], Or(~x[0], x[1])), Or(~x[2], Or(~x[0], x[1])), Or(x[2], Or(~x[0], ~x[1]))]
# Each term represents of the list represents the max term (prime implicant)
print (h)
#h is the POS representation of g
k = compute_robdd_to_f(12)
k_list = []
print (compute_robdd_to_f(12))
compute_shannon(k,k_list,X,0,n)
z = one
for i in k_list:
	z = z & i
print ("k_list",k_list)
print (z)
#h is the POS representation of g
