C from pyeda.inter import *
>>> x0 = exprvar('x0')
>>> x1 = exprvar('x1')
>>> x2 = exprvar('x2')
>>> x3 = exprvar('x3')
>>> h1 = expr('x0|x1')
>>> f1 = expr( '(x3&x2&h1_rhs)|(x3&~x2&~h1_rhs)')
>>> f2_bar = expr('(~x3)&(x2^h1_rhs)')
>>> f = expr('f1_rhs|f2_bar_rhs')
 print(f)
Or(f1_rhs, f2_bar_rhs)
>>> h1_rhs = exprvar('h1_rhs')
>>> f1_rhs = exprvar('f1_rhs')
>>> f2_bar_rhs =exprvar('f2_bar_rhs')
>>> f1_flattered =f1.compose({h1_rhs:h1})
>>> f2_bar_flattered = f2_bar.compose({h1_rhs:h1})
>>> f_flattered = f.compose({f2_bar_rhs:f2_bar_flattered,f1_rhs:f1_flattered})
>>> g = expr('x3?(x2?h1_rhs:~h1_rhs):(x2?~h1_rhs:h1_rhs)')
>>> print(g)
ITE(x3, ITE(x2, h1_rhs, ~h1_rhs), ITE(x2, ~h1_rhs, h1_rhs))
//test vector generation
>>> f_fault_free = f_flattered
// generate faulty version of f using compose operations (stuck at fault)
//
//Recursion
