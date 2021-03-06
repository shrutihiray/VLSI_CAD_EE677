from pyeda.inter import * 
a, b, c, d = map(exprvar, "abcd")
n=8
X = exprvars('x', n)
zero = expr(0)
one = expr(1)

f1 = Or(~a & ~b & ~c, ~a & ~b & c, a & ~b & c, a & b & c, a & b & ~c)
f1m = espresso_exprs(f1)
print(f1)
print(f1m)
f_list = []
#restricting
f2 = expr('a|b|c')
f3 = f2.restrict({a: zero})
f4 = f2.restrict({a: one})
f_list.append(f3)
print ("f is")
print (f_list)
f_list.append(f4)
print ("f is")
print (f_list)

f5 = expr('x[1]|x[2]|x[3]')
f6 = expr(X[1]) | f5.restrict({X[1]: zero})
f7 = expr('~x[2]') | f5.restrict({X[2]: zero})
f8 = f5.restrict({X[4]:zero})
print ("f8 is")
print (f8)
f9 = f5.restrict({X[4]:one})
print ("f9 is")
print (f9)
if(f9==f8):
	print("In here")
else:
	print("NOt here")
f_list.append(f6)
print ("f6 is")
print (f6)
f_list.append(f7)
print ("f is")
print (f_list)
f_list = []
def compute_shannon(f,f_list,X,i,n):
	f_E_i = f.restrict({X[i]: zero})
	if(f_E_i != one ):
		f_E = expr('x[i]') | f_E_i
		if(i==n-1):
			f_list.append(f_E)
		else:
			compute_shannon(f_E,f_list,X,i+1,n)
	f_T_i = f.restrict({X[i]: one})    
	if(f_T_i != one ):
		f_T = expr('~x[i]') | f_T_i
		if(i==n-1):
			f_list.append(f_T)
		else:
			compute_shannon(f_T,f_list,X,i+1,n)	
	return
				
	

g = expr('(x[4]&x[5]|x[6])')
#compute_shannon(g,f_list,X,0,8)	
x0 = exprvar('x0')
x1 = exprvar('x1')
x2 = exprvar('x2')
x3 = exprvar('x3')
h1 = expr('x0|x1')
f1 = expr( '(x3&x2&h1_rhs)|(x3&~x2&~h1_rhs)')
f2_bar = expr('(~x3)&(x2^h1_rhs)')
f = expr('f1_rhs|f2_bar_rhs')
print(f)

h1_rhs = exprvar('h1_rhs')
f1_rhs = exprvar('f1_rhs')
f2_bar_rhs =exprvar('f2_bar_rhs')
f1_flattered =f1.compose({h1_rhs:h1})
f2_bar_flattered = f2_bar.compose({h1_rhs:h1})
f_flattered = f.compose({f2_bar_rhs:f2_bar_flattered,f1_rhs:f1_flattered})
g = expr('x3?(x2?h1_rhs:~h1_rhs):(x2?~h1_rhs:h1_rhs)')
print(g)
ITE(x3, ITE(x2, h1_rhs, ~h1_rhs), ITE(x2, ~h1_rhs, h1_rhs))
f_fault_free = f_flattered
