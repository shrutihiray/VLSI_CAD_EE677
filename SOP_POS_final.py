from pyeda.inter import *

#used previously calculated functions to find SOP_to_POS
#find POS_of_f_complement using SOP_to_POS_comple function
#then find SOP_of_f_complement from POS_of_f_complement using POS_to_SOP_direct function
#and at last POS_of_f from SOP_of_f_complement using SOP_to_POS_comple function

def SOP_POS_indirect(f):
	SOP_POS_comple_f=SOP_to_POS_comple(f)
	POS_SOP_comple_f=POS_SOP_direct(SOP_POS_comple_f)
	SOP_POS_comple_comple_f=SOP_to_POS_comple(POS_SOP_comple_f)
	return SOP_POS_comple_comple_f


def SOP_to_POS_comple(f):
	s=str(f)
	s=s.replace("Or","g")
	s=s.replace("And","h")
	mystack=[]

#whenever we encounter ")" ,we need to pop till we get g or h(i.e. either AND or OR) and evaluate and then push back on stack
#in evauation g is replaced by h and h by g,also each operand is inverted(i.e. a is now ~a and vice-versa)
	for i in s:
		mystack.append(i)
		#if ")" is encountered we need to evaluate
		if(i==")"):
		
			temp=""
			j=mystack.pop()
			#pop till we read the operation(g or h)
			#each literal is negated
			
			while(j!="g" and j!="h"):
			
				
			
				if(len(j)!=1):
					temp=temp+j
				else:
					temp=temp+"~"+j
				j=mystack.pop()
	  			
			
			#And becomes Or ,Or becomes And
			if(j=="g"):
				flag="h"
			if(j=="h"):
				flag="g"
			
			#along with literal, other elements like {"(",")"","," " } also get negated9as they are also on stack) and therefore 				need to be corrected
			# id literal is ~b the what we get from above is "~b~~",which is to be corrected to "b"
			count=0  #no. of times such cases are corrected
			p=temp
			for i in range(len(temp)-1):
				if(p[i-3*count]=="~" and p[i+1-3*count]=="~"):
					p=p[:i-2-3*count]+p[i-1-3*count]+p[i+2-3*count:]
					count=count+1
			
			temp=p
			#correcting "~)" to "("{as pop in reverse order of push} and "~(" to ")" in case the updated operation is g(i.e. Or) 				because it needs priority to be mentioned
			#else we correct "~)" and "~)" to "" 
			
			if(flag=="g"):
				temp=temp.replace("~)","lp")
				temp=temp.replace("~(","rp")
							
			else:
				temp=temp.replace("~(","")
				temp=temp.replace("~)","")
			temp=temp.replace("lp","(")
			temp=temp.replace("rp",")")

			#insering operation
			temp=temp.replace("~ ~,",flag)
			
			#push the evaluated value on the stack
			mystack.append(temp)
	
	#pop the final evaluated value		
	expression=mystack.pop()
	expression=expression.replace("g","|")
	expression=expression.replace("h","&")
	g=expr(expression)
	return g

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

f=expr("a|(b&c)|(~b&d)")
print(f)
expression=SOP_POS_indirect(f)
print(expression)


