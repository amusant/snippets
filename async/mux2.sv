module mux2(a,b, sel, s);
parameter DW=1;
input bit [DW-1:0] a;
input bit [DW-1:0] b;
input bit sel;
output bit [DW-1:0] s;



always@(*)
	if(sel==1'b0) s<= #1ps a;
	else if(sel==1'b1) s<= #1ps b;
	else s<= #1ps 1'bx;
endmodule
