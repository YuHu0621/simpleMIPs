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

for counter in range(0, 5):
	mips = circuits.simpleMIPS(register_file_0)
	out_mips = mips.getCircuitOutput(test_instruction_sequence[counter])
	print out_mips
