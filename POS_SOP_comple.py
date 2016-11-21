from pyeda.inter import *

#function to convert POS(f) to SOP(complement_f) 
def POS_to_SOP_comple(f):
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
			#correcting "~)" to "("{as pop in reverse order of push} and "~(" to ")" in case the updated operation is h(i.e. Or) 				because it needs priority to be mentioned
			#else we correct "~)" and "~)" to "" 
			if(flag=="h"):
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


f=expr("a&(~c|v)&(~d|~a)")
print (f)
g=POS_to_SOP_comple(f)
print (g)	

