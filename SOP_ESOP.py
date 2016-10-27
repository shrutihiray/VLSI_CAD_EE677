from pyeda.inter import *

#function to remove reoccurences in a string
def removeDuplicates(string):
    result=[]
    seen=set()
    for char in string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

#function to convert SOP to ESOP
def SOP_to_ESOP(f):
	s=str(f)
	
#if ~literal is present,it's modelled as LITERAL to distinguish between Literal and its negation 
	for i in range(len(s)):
		if(s[i]=="~"):
			s=s[:i+1]+s[i+1].upper()+s[i+2:]
	s=s.replace("~","")
	

#And is replaced with char 'g' for simplicity and splitting string to get list
	s=s[3:len(s)-1]
	s=s.replace("And","g")
		
	for i in range(len(s)):
		if(s[i]==","):
			if(s[:i+1].count("(")%2==s[:i+1].count(")")%2):
				s=s[:i]+";"+s[i+1:]		
	
	s=s.split(";")
	
	for i in range(len(s)):
		s[i]=s[i].replace(" ","")
	#print(s)

#when And is not present i.e. if only one term is present to be ORed with others(ex:OR(a,b,And(c,a))
#single term a can be modelled as: And(a,1)
	for i in range(len(s)):
		if(len(s[i])==1 or len(s[i])==2):
			s[i]="g("+s[i]+",1)"

	for i in range(len(s)):
		s[i]=s[i][2:len(s[i])-1]
		s[i]=s[i].replace(",","g")
	
#Reed Muller algo
	inilen=len(s)
	i=0
	j=0
	while(i<inilen):
		templen=len(s)
		j=0
		while(j<templen):
			if(j!=i):
				
				s.append(str(s[i]+"g"+s[j]))
			j=j+1
		i=i+1
	
#sorting and removing duplicates in an object of list

	for i in range(len(s)):
		s[i]=s[i].replace("g","")
		s[i]=removeDuplicates(s[i])
		words=[]
		for j in range(len(s[i])):
			words.append(s[i][j])
		words.sort()
		m="0"
		for j in range(len(words)):
			m=m+words[j]+"g"
		s[i]=m[1:len(m)-1]
	

#(1 and something) = something
	for i in range(len(s)):
		s[i]=s[i].replace("1g","")
	
#sorting and removing duplicates in list according to XOR property
	temp_list=[]
		
	for i in range(len(s)):
		flag=0
		if(s.count(s[i])%2!=0):
			
			for j in temp_list:
				if(j==s[i]):
					flag=1

			if(flag==0):
				temp_list.append(s[i])
		
#preparing the expression (input to boolean function formation)from this list 
	expression="0"
	for i in range(len(temp_list)):
		expression=expression+temp_list[i]+"^"	


	expression=expression[1:len(expression)-1]
	expression=expression.replace("g","&")

#Restoring negation symbol from capital literal	
	for i in range(len(expression)):
		if(expression[i].isupper()):
			expression=expression[:i]+"~"+expression[i].lower()+expression[i+1:]		


	g=expr(expression)
	
	return g
#main
f=expr("~a&b|b&c|c&d")
g=SOP_to_ESOP(f)
print (g)	



