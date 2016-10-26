from pyeda.inter import * 
zero = expr(0)
one = expr(1)
f_list = [] #List contains all the required max-terms

def compute_shannon(f,f_list,X,i,n):
	f_E_i = f.restrict({X[i]: zero})
	f_T_i = f.restrict({X[i]: one})
	#print (i)
	if(f_E_i == f_T_i):
		#print("f",f,"In here")
		#print (X[i])
		if(f_E_i != one): #No need to proceed if value is one
			if(i==n-1):
				f_list.append(f)  #Only leaf nodes are appended
			else:
				compute_shannon(f,f_list,X,i+1,n) 
	else:
		if(f_E_i != one ): #No need to proceed if value is one
			f_E = expr(X[i]) | f_E_i
			#print("i",i,"f_E",f_E)
			if(i==n-1):
				
				f_list.append(f_E) #Only leaf nodes are appended
			else:
				compute_shannon(f_E,f_list,X,i+1,n)	 
		if(f_T_i != one ): #No need to proceed if value is one
			f_T = expr(~X[i]) | f_T_i
			#print("i",i,"f_T",f_T)
			if(i==n-1):
				
				f_list.append(f_T) #Only leaf nodes are appended
			else:
				compute_shannon(f_T,f_list,X,i+1,n)	
	return

n=3
X = exprvars('x', n)
g = expr('(x[0]&(x[1]|x[2]))')
compute_shannon(g,f_list,X,0,n)
print (f_list)
