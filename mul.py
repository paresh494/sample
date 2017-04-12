#! /usr/bin/python
import copy


def mul(a,b,c):
        if c==len(b):
		return ""	
	f = len(a)-1
	h = len(b)-1
	g = list(copy.deepcopy(a))
	m=0	
	o=0
	carry=0
	for i in range(0,len(a)):
		#print i		
		if m!=0:
			o = m
			m = 0 
		y = int(a[f-i]) * int(b[c])
		if y/10 != 0 or o!=0:
			o = o + y%10			
			m = y/10
			if o/10!=0:
				o1= o%10
				m = m + o/10
				g[f-i] = str(o1)			
			else:				
				g[f-i] = str(o)
	 	 
		else:
			g[f-i] = str(y)
		o=0
	if m!=0:
		g = str(m) + "".join(g)
	yu = copy.deepcopy("".join(g))
	
	for op in range(0,len(b)-c-1):
		yu = yu + "0"        
	yu = list(yu)	
	yulen = len(yu)
	#print yu
	l = mul(a,b,c+1)
	m=0
	for e in range(0,len(l)):
		if m!=0:
			o = m
			m=0
		y = int(l[len(l)-e-1]) + int(yu[yulen-e-1])
		if y/10 != 0 or o!=0:
			o = o + y%10			
			m = y/10
			if o/10!=0:
				o1= o%10
				m = m + o/10
				yu[yulen-e-1] = str(o1)			
			else:				
				yu[yulen-e-1] = str(o)
	 	 
		else:
			yu[yulen-e-1] = str(y)
		o=0
	if m!=0 and len(yu)>len(l):
		 for pp in range(0,len(yu)-len(l)):
		    if m==0:
			break 
		    y = m + int(yu[len(yu) - len(l) - pp - 1])
		    m=0
		    if y/10 != 0 or o!=0:
			o = o + y%10			
			m = y/10
			if o/10!=0:
				o1= o%10
				m = m + o/10
				yu[len(yu) - len(l) - pp - 1] = str(o1)			
			else:				
				yu[len(yu) - len(l) - pp - 1] = str(o)
	 	 
		    else:
			yu[len(yu) - len(l) - pp - 1] = str(y)
		    o=0
				
		 if m!=0:
		  #print "happe"	
		  yu = str(m) + "".join(yu) 
				 

	#print "".join(yu)	
	return "".join(yu)
a = raw_input("a = ")
b = raw_input("b = ")
print mul(a,b,0)		
		
		 
		
