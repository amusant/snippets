module testbench;



wire [0:1] i,j,k,l;
wire [7:0] idata,jdata,kdata;
wire [7:0] ldata;

reg [0:1] i_reg,j_reg,k_reg,l_reg;
reg [7:0] idata_reg,jdata_reg,kdata_reg;
reg [7:0] ldata_reg;
assign i[0] = i_reg[0];
assign j[0] = j_reg[0];
assign k[0] = k_reg[0];
assign l[1] = l_reg[1];
assign i_reg[1] = i[1];
assign j_reg[1] = j[1];
assign k_reg[1] = k[1];
assign l_reg[0] = l[0];

MUX22_HS DUT(i,idata_reg,j,jdata_reg,k,kdata_reg,l,ldata);


logic [7:0] idata_f[0:100];
real idelay[0:100];


logic [7:0] jdata_f[0:100];
real jdelay[0:100];

logic [7:0] kdata_f[0:100];
real kdelay[0:100];

logic [7:0] ldata_f[0:100];
real ldelay[0:100];
logic istate=1'b0;
initial begin 
	int count;
	automatic integer fid = $fopen("i.txt", "r"); 
     integer retval;
	 string line;
	while (!$feof(fid)) begin
	   retval=$fgets (line, fid);
	   if (line[0]== 35) continue;
	   retval=$sscanf (line, "%f\t%x", idelay[count],idata_f[count]);
		if(retval) begin
	   		$display("READ FLIE I %f:%X\n",idelay[count],idata_f[count]);
	    	count=count+1;
		end
	end
	i_reg[0]=1'b0;
	#10
	for (int i=0; i<count-1; i++) begin
		#(idelay[i]);
		idata_reg=idata_f[i];
		i_reg[0]=~i_reg[0];
		do begin
			#1ns;
		end
		while (istate==i_reg[1]); 
			istate =i_reg[1]; 
	end
end

logic jstate=1'b0;
initial begin 
	int count;
	automatic integer fid = $fopen("j.txt", "r"); 
     integer retval;
	 string line;
	while (!$feof(fid)) begin
	   retval=$fgets (line, fid);
	   if (line[0]== 35) continue;
	   retval=$sscanf (line, "%f\t%x", jdelay[count],jdata_f[count]);
	   	$display("READ FLIE J %f:%X\n",jdelay[count],jdata_f[count]);
	   count=count+1;
	end
	j_reg[0]=1'b0;
	#10
	for (int i=0; i<count-1; i++) begin
		#(jdelay[i]);
		jdata_reg=jdata_f[i];
		j_reg[0]=~j_reg[0];
		do begin
			#1ns;
		end
		while (jstate==j_reg[1]); 
		jstate =j_reg[1]; 
	end
end

logic kstate=1'b0;
initial begin 
	int count;
	automatic integer fid = $fopen("k.txt", "r"); 
     integer retval;
	 string line;
	while (!$feof(fid)) begin
	   retval=$fgets (line, fid);
	   if (line[0]== 35) continue;
	   retval=$sscanf (line, "%f\t%x", kdelay[count],kdata_f[count]);
	   	$display("READ FLIE K %f:%X\n",kdelay[count],kdata_f[count]);
	   count=count+1;
	end
	k_reg[0]=1'b0;
	#10
	for (int i=0; i<count-1; i++) begin
		#(kdelay[i]);
		kdata_reg=kdata_f[i];
		k_reg[0]=~k_reg[0];
		do begin
			#1ns;
		end
		while (kstate==k_reg[1]); 
			kstate =k_reg[1]; 
	end
end

logic lstate=1'b0;
initial begin 
	int count;
	automatic integer fid = $fopen("l.txt", "r"); 
     integer retval;
	 string line;
	$dumpfile("dump.vcd");$dumpvars;
	while (!$feof(fid)) begin
	   retval=$fgets (line, fid);
	   if (line[0]== 35) continue;
	   retval=$sscanf (line, "%f\t%x", ldelay[count],ldata_f[count]);
	   	$display("READ FLIE K %f:%X\n",ldelay[count],ldata_f[count]);
	   count=count+1;
	end
    l_reg[1]=1'b0;	
	#10
	for (int i=0; i<count-1; i++) begin
		do begin
			#1ns;
		end
		while (lstate==l_reg[0]); 
		#(ldelay[i]);
			l_reg[1]=~l_reg[1];
			lstate=l_reg[1];
	end
    //$dumpvars;
    #100ns;
	$stop;
end
endmodule

