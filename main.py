from pyeda.inter import * 
from SOP_POS_final import *
from SOP_POS_comple import *
from POS_SOP_final import *
from POS_SOP_comple import *
from SOP_ESOP import *

#TEST_CASE Printing all canonical forms
print(" ")
f=expr("a|(~b&c)|(~b&~d)")
print (f)
print ("SOP_to_POS_comple:",SOP_to_POS_comple(f))
print (" ")
f=expr("a&(~c|v)&(~d|~a)")
print (f)
print ("POS_to_SOP_comple:",POS_to_SOP_comple(f))
print (" ")
f=expr("~x1&(~x2|x3)&(x2|x5)")
print (f)
print("POS_to_SOP:",POS_SOP_direct(f))
print (" ")
f=expr("a|(b&c)|(~b&d)")
print (f)
print("SOP_to_POS:",SOP_POS_indirect(f))
print(" ")
f=expr("~x1|x2&~x3|x3&x4")
print (f)
g=SOP_to_ESOP(f)
print ("SOP_to_ESOP:",SOP_to_ESOP(f))	
print(" ")

