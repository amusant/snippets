module latch(q,en,d);
parameter n=8;
input bit [n-1:0]  q;
input en;
output bit [n-1:0] d; 
always@(*) 
	if(en==1'b1) d<=q;
	else d<=d;
endmodule
