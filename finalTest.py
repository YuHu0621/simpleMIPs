__author__ = "YuHu, Yueming Yang"
__Copyright__ =  "Copyright @2016, Mount Holyoke College"

import circuits

register_file_0 = []
for counter in range(0,32):
	register = []
	for counter in range(0,32):
		if counter == 30:
			register.append(1)
		else: 
			register.append(0)
	register_file_0.append(register)

regFile = circuits.registerFile(register_file_0)
out_regFile = regFile.getAllRegValues()


test_instruction_sequence = []

#sw_01 = [1,0,1,0,1,1, 1,0,0,0,0, ]
#lw = [1,0,0,0,1,1,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
#add $a2 $a3 $t0 
#or $t0 $a3 $t1
#add $t1 $t1 $t2
#and $t3 $t1 $t2
#slt $v0 $t2 $v0
#sw $t0 3($t3)
add_sequence = [0,0,0,0,0,0, 0,0,1,1,0, 0,0,1,1,1, 0,1,0,0,0, 0,0,0,0,0, 1,0,0,0,0,0]
or_sequence = [0,0,0,0,0,0, 0,1,0,0,0, 0,0,1,1,1, 0,1,0,0,1, 0,0,0,0,0, 1,0,0,1,0,1]
add_sequence_01 =[0,0,0,0,0,0, 0,1,0,0,1, 0,1,0,0,1, 0,1,0,1,0, 0,0,0,0,0, 1,0,0,0,0,0]
and_sequence = [0,0,0,0,0,0, 0,1,0,0,1, 0,1,0,1,0, 0,1,0,1,1, 0,0,0,0,0, 1,0,0,1,0,0]
slt_sequence = [0,0,0,0,0,0, 0,0,0,1,0, 0,1,0,1,0, 0,0,0,1,0, 0,0,0,0,0, 1,0,1,0,1,0]
sw_sequence = [1,0,1,0,1,1, 0,1,0,0,0, 0,1,0,1,1, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]
lw_sequence = [1,0,0,0,1,1, 0,1,0,0,0, 0,0,0,0,1, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]
mips = circuits.simpleMIPS(regFile)
out_mips = mips.getCircuitOutput(add_sequence)
#print "register file: ", out_mips[0]
print "add_cal: ", out_mips[2]
print " "
print " "
print " "
out_mips = mips.getCircuitOutput(or_sequence)
print "or: ", out_mips[2]
print " "
print " "
print " "

out_mips = mips.getCircuitOutput(add_sequence_01)
print "add_cal: ", out_mips[2]
print " "
print " "
print " "

out_mips = mips.getCircuitOutput(and_sequence)
print "and_cal: ", out_mips[2]
print " "
print " "
print " "

out_mips = mips.getCircuitOutput(slt_sequence)
print "slt_cal: ", out_mips[2]
print " "
print " "
print " "

out_mips = mips.getCircuitOutput(sw_sequence)
print "sw_cal: ", out_mips[2]
print " "
print " "
print " "

out_mips = mips.getCircuitOutput(lw_sequence)
print "lw_cal: ", out_mips[2]
print " "
print " "
print " "

'''
for counter in range(0, 1):
	mips = circuits.simpleMIPS(register_file_0)
	out_mips = mips.getCircuitOutput(test_instruction_sequence[counter])
	print "register file: ", out_mips[0]
	#print "memory: ", out_mips[1]
	print "out_cal: ", out_mips[2]
'''
#print out_mips[0]
#print out_mips[1]
#print out_mips[2]