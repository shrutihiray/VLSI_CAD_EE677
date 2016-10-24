from pyeda.inter import * 
a, b, c, d = map(exprvar, "abcd")
f1 = Or(~a & ~b & ~c, ~a & ~b & c, a & ~b & c, a & b & c, a & b & ~c)
f1m = espresso_exprs(f1)
print (f1m)
