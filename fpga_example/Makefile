VPR=
ODIN=
ARCH=./vtr_flow/arch/timing/k6_N10_40nm.xml

all:
	$(ODIN) -a $(ARCH) -V ./minijazz/minijazztestnaddernet.sv -o  testnaddernet.blif
	$(VPR) $(ARCH) testnaddernet.blif  --route_chan_width 10  --disp on --timing_analysis on
testnaddernet.sv:
	python3 mjtovlog.py test/nadder.net
