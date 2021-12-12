#!/usr/bin/python
import re,sys
inputs={}
outputs={}
netlist={}
netwidth={}
def parse(mjfile):
	data=open(mjfile)
	line=data.readline()
	while(line):
		format=re.search('INPUT',line)
		if(format):
			print("Reading Inputs")
			line=line.replace("INPUT","")
			line=line.replace(" ","")
			line=line.replace("\n","")
			for i  in (line.split(',')):
				print(line.split(','))
				print(i)
				inputs[i]='input'
		format=re.search('OUTPUT',line)
		if(format):
			print("Reading Outputs")
			line=line.replace("OUTPUT","")
			line=line.replace(" ","")
			line=line.replace("\n","")
			for i  in (line.split(",")):
				if(i!='OUTPUT'):
					outputs[i]='output'
		format=re.search('VAR',line)
		if(format):
			line=data.readline()
			while(not re.search('IN',line)):
				line=line.replace(" ","")
				line=line.replace("\n","")
				#print(line.split(','))
				for i  in (line.split(',')):
					if(i!=""):
						if(len(i.split(':')) > 1 ):
							#print(i.split(':'))
							if(i.split(':')[0] in inputs.keys()):
								print(i.split(':')[0])
								inputs[i.split(':')[0]]=i.split(':')[1]
								#netwidth[i.split(':')[0]]=i.split(':')[1]
							elif (i.split(':')[0] in outputs.keys()):
								outputs[i.split(':')[0]]=i.split(':')[1]
								#netwidth[i.split(':')[0]]=i.split(':')[1]
							else:
								netlist[i.split(':')[0]]=i.split(':')[1]
								#netwidth[i.split(':')[0]]=i.split(':')[1]
						else:
							if(i.split(':')[0] in inputs.keys()):
								inputs[i.split(':')[0]]='0'
							elif (i.split(':')[0] in outputs.keys()):
								outputs[i.split(':')[0]]='0'
							else:
								netlist[i.split(':')[0]]='0'
							#netwidth[i.split(':')[0]]=0

				line=data.readline()
				#print(line)
		
		line=data.readline()
	data.close()
	modulename=mjfile.replace('/','')
	modulename=modulename.replace('.','')
	with open(modulename+'.sv', 'w') as fout:
		print("module %s (" %( modulename) ,file=fout)
		for i in inputs:
			if(inputs[i]=='0'):
				print("input logic %s," % (i),file=fout)
			else:
				print("input logic [%s-1:%s] %s," % (inputs[i],'0',i),file=fout)
		cnt=0
		for i in outputs:
			cnt=cnt+1
			if(cnt!=len(outputs)):
				if(outputs[i]=='0'):
					print("output logic %s," % (i),file=fout)
				else:
					print("output logic [%s-1:%s] %s," % (outputs[i],'0',i),file=fout)
			else:
				if(outputs[i]=='0'):
					print("output logic %s" % (i),file=fout)
				else:
					print("output logic [%s-1:%s] %s" % (outputs[i],'0',i),file=fout)
		print(");",file=fout)
		for i in netlist:
			if(netlist[i]!='0'):
				print("logic [%s:%s] %s;" % (netlist[i], 0,i ),file=fout)
			else:
				print("logic %s;" % (i),file=fout)


		#write the gates as eqn with assign
		data=open(mjfile)
		line=data.readline()
		while(line):
			format=re.search("(.*)=\s*([A-Z]+)(.*)",line)
			if(format):
				OP=format.group(2)
				lhs= format.group(1)
				rhs=format.group(3)
				if(OP=='SELECT'):
					print(OP,lhs,rhs)
					sel,op=rhs.split()
					print("assign %s=%s[%s];" % (lhs,op,sel) ,file=fout)
				elif(OP=='SLICE'):
					print(OP,lhs,rhs)                                               
					ilow,ihigh,op=rhs.split()                                       
					print("assign %s=%s[%s:%s];" % (lhs,op,ihigh,ilow) ,file=fout)  
				elif(OP=='CONCAT'):
					print(OP,lhs,rhs)                                               
					op1,op2=rhs.split()                                       
					print("assign %s={%s,%s};" % (lhs,op2,op1) ,file=fout)  
				elif(OP=='AND'):
					print(OP,lhs,rhs)                                               
					op1,op2=rhs.split()                                       
					print("assign %s=%s && %s;" % (lhs,op1,op2) ,file=fout)  
				elif(OP=='XOR'):
					print(OP,lhs,rhs)                                               
					op1,op2=rhs.split()                                       
					print("assign %s=%s ^ %s;" % (lhs,op1,op2) ,file=fout)  
				elif(OP=='OR'):
					print(OP,lhs,rhs)                                               
					op1,op2=rhs.split()                                       
					print("assign %s=%s || %s;" % (lhs,op1,op2) ,file=fout)  
			else:
				format=re.search("(.*)=\s*(.*)",line)
				if(format):
					lhs= format.group(1)
					rhs=format.group(2)
					print(lhs,rhs)
					print("assign %s=%s;" % (lhs,rhs) ,file=fout)
			line=data.readline()

		print("endmodule",file=fout)
parse(sys.argv[1])
