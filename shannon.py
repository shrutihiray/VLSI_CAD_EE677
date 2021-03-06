from pyeda.inter import * 

#AUTHOR: SHRUTI HIRAY, 14d070016
zero = expr(0)
one = expr(1)
f_list = [] #List contains all the prime implicants required for POS form

#Function computes the max terms and minimises it i.e (x0 | x1)(x0 | ~x1) is redundant and can be expressed as (x0). Not necessary upto optimum level
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


# Example Case
n=3
X = exprvars('x', n)
g = expr('(x[0]&x[1]&x[2])')
f_list = []
h = one
compute_min_shannon(g,f_list,X,0,n)
for i in f_list:
	h = h & i
print (f_list)
#Output is as follows:
#[Or(x[0], 0), Or(x[2], Or(~x[0], x[1])), Or(~x[2], Or(~x[0], x[1])), Or(x[2], Or(~x[0], ~x[1]))]
# Each term represents of the list represents the max term (prime implicant)
print (h)
#h is the POS representation of g
