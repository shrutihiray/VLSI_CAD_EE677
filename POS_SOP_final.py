from pyeda.inter import *

def POS_SOP_direct(f):
	s=str(f)
	#if ~literal is present,it's modelled as LITERAL to distinguish between Literal and its negation 
	for i in range(len(s)):
		if(s[i]=="~"):
			s=s[:i+1]+s[i+1].upper()+s[i+2:]
	s=s.replace("~","")

	#converting Or(_,_,_) to (_;_;_) 
	p=s
	count=0
	for i in range(len(s)):
		if (s[i]=="O"):
			for j in range(i+1,len(s)):
				if(s[j]==")"):
					s1=s[i+2:j+1]					
					s1=s1.replace(",",";")
					p=p[:(i-2*count)]+s1+p[j+1-2*count:]					
					break
			count=count+1
	
	#convering And(___________) to ___________ 
	s=p[4:len(p)-1]
	#splitting each maxterm
	s=s.split(",")
	mystack=[]
	#splitting each minterm inside a maxterm
	s[0]=s[0].replace(";",",")
	mystack.append(s[0])
	#first pop from stack ,compute (poped term).(next maxterm of s) and after computing the minterms push pack the evaluated SOP form 		into the stack
	for i in range(1,len(s)):
		s1=mystack.pop()
		s1=s1.replace("(","")
		s1=s1.replace(")","")
		s1=s1.split(",")
		p1=s[i]
		p1=p1.replace("(","")
		p1=p1.replace(")","")
		p1=p1.replace(";",",")
		p1=p1.split(",")
		final="0"
		for k in s1:
			for m in p1:
				final=final+k+"g"+m+","
			
		final=final[1:len(final)-1]
		mystack.append(final)

	#pop the final evaluated SOP from the stack  
	s=mystack.pop()
	s=s.replace("g ","&")
	expression=s.replace(",","|")
	
	#Restoring negation symbol from capital literal
	expressionfinal=""	
	for i in range(len(expression)):
		if(expression[i].isupper()):
			
			expressionfinal=expressionfinal+"~"+expression[i].lower()
		else:
			expressionfinal=expressionfinal+expression[i]
	expressionout=expr(expressionfinal)
	return expressionout

f=expr("~x1&(~x2|x3)&(x2|x5)")
POS_SOP=POS_SOP_direct(f)
print(POS_SOP)
		
