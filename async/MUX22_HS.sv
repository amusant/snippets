module MUX22_HS(i,idata,j,jdata,k,kdata,l,ldata);
inout logic [0:1] i,j,k,l;
input logic [7:0] idata,jdata,kdata;
output logic [7:0] ldata;
logic [7:0] ldata_int,kdata_latch;

logic sig0,sig1,sig2,sig3;
logic [1:0] ki,kj;


// K to ki and kj
latch #(8) latchk(kdata,en,kdata_latch);
assign sig4= k[0] ^ ki[0];
assign sig5= k[0] ^ kj[0];
mux2 #(1) mux1(kj[0],sig4,kdata[0],kj[0]);
mux2 #(1) mux2(sig5 ,ki[0],kdata[0],ki[0]);


celement cel0(kj[0],j[0],~sig0,sig1);
celement cel1(~sig2,ki[0],i[0],sig3);
assign sig0 = l[1] ^ sig3;
assign sig2 = l[1] ^ sig1;

assign #1 j[1] =  sig1;
assign #1 i[1] =  sig3;

assign k[1] = i[1] ^ j[1];

assign en =(k[1]^ l[1]);

assign l[0] = k[1];

mux2 #(8) mux_data(idata,jdata,kdata[0],ldata_int);
latch #(8) l0(ldata_int,en,ldata);
endmodule
