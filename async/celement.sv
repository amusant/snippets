module celement(input  bit a, input  bit b, input  bit c, output  bit s);

always@(*) begin
	if(a==b && b==c) 
	#1ps s<=a;
end
endmodule
