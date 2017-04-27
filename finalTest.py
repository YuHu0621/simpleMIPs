__author__ = "YuHu, Yueming Yang"
__Copyright__ =  "Copyright @2016, Mount Holyoke College"

import circuits

register_file_0 = []
for counter in range(0,32):
	register = []
	for counter in range(0,32):
		if counter == 31:
			register.append(1)
		register.append(0)
	register_file_0.append(register)

regFile = circuits.registerFile(register_file_0)
out_regFile = regFile.getAllRegValues()


test_instruction_sequence = [[0,0,0,0,0,0, 0,0,1,1,0, 0,0,1,1,1, 0,1,0,0,0, 0,0,0,0,0, 1,0,0,0,0,0], [0,0,0,0,0,0, 0,1,0,0,0, 0,0,1,1,1, 0,1,0,0,1, 0,0,0,0,0, 1,0,0,1,0,1], [0,0,0,0,0,0, 0,1,0,0,1, 0,1,0,0,1, 0,1,0,1,0, 0,0,0,0,0, 1,0,0,0,0,0], [0,0,0,0,0,0, 0,1,0,0,1, 0,1,0,1,0, 0,1,0,1,1, 0,0,0,0,0, 1,0,0,1,0,0],[0,0,0,0,0,0, 0,0,0,1,0, 0,1,0,1,0, 0,0,0,1,0, 0,0,0,0,0, 1,0,1,0,1,0]]

#sw_01 = [1,0,1,0,1,1, 1,0,0,0,0, ]
#lw = [1,0,0,0,1,1,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
#add $a2 $a3 $t0 
#or $t0 $a3 $t1
#add $t1 $t1 $t2
#and $t1 $t2 $t3
#slt $v0 $t2 $v0

for counter in range(0, 5):
	mips = circuits.simpleMIPS(register_file_0)
	out_mips = mips.getCircuitOutput(test_instruction_sequence[counter])
	#print "register file: ", out_mips[0]
	#print "memory: ", out_mips[1]
	print "out_cal: ", out_mips[2]

#print out_mips[0]
#print out_mips[1]
#print out_mips[2]