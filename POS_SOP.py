from pyeda.inter import *

#function to convert POS to SOP to ESOP
def POS_to_SOP(f):
	s=str(f)
	s=s.replace("And","g")
	s=s.replace("Or","h")
	print(s)
	mystack=[]

#whenever we encounter ")" ,we need to pop till we get g or h(i.e. either AND or OR) and evaluate and then push back on stack
#in evauation g is replaced by h and h by g,also each operand is inverted(i.e. a is now ~a and vice-versa)
	for i in s:
		if(i!=")"):
			mystack.append(i)
		
		else:	
			temp=""
			j=mystack.pop()
			while(j!="g" and j!="h"):
			
				
			
				if(len(j)!=1):
					temp=temp+j
				else:
					temp=temp+"~"+j
				j=mystack.pop()
	  			
			

			if(j=="g"):
				flag="h"
			if(j=="h"):
				flag="g"
		
			print(temp)
			temp=temp.replace("~(","")
			temp=temp.replace("~ ~,",flag)
			mystack.append(temp)
	print(mystack)	
	expression=mystack.pop()
	expression=expression.replace("~~","~")
	expression=expression.replace("g","&")
	expression=expression.replace("h","|")
	g=expr(expression)
	return g

f=expr("a&(c|v)&d")
g=POS_to_SOP(f)
print (g)
			
			
		

