__author__ = "Yu Hu, Yueming Yang"
__Copyright__ = "Copyright @2016, Mount Holyoke College"

import circuits
#32 bit arrays for test
A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]

#testing aluControl for add, ALUOp is 10, function filed is 100000
test_aluControl_add = [1, 0, 1, 0, 0, 0, 0, 0]

test_aluControls = test_aluControl_add
aluControl = circuits.aluControl(test_aluControls)
#aluCtl
out_aluControl = aluControl.getCircuitOutput()
opCode = out_aluControl[0]
cin = out_aluControl[1]
alu_32bit = circuits.ALU_32bit(A, B, cin, opCode)
out_alu_addition = alu_32bit.getCircuitOutput()
print out_alu_addition, "under signal ", test_aluControls, " for addition"

#testing aluControl for sub, ALUOp is 10, function filed is 100010
test_aluControl_sub = [1, 0, 1, 0, 0, 0, 1, 0]

test_aluControls = test_aluControl_sub
aluControl = circuits.aluControl(test_aluControls)
#aluCtl
out_aluControl = aluControl.getCircuitOutput()
opCode = out_aluControl[0]
cin = out_aluControl[1]
alu_32bit = circuits.ALU_32bit(A, B, cin, opCode)
out_alu_sub = alu_32bit.getCircuitOutput()
print out_alu_sub, "under signal ", test_aluControls, " for subtraction"

#testing aluControl for AND, ALUOp is 10, function filed is 100100
test_aluControl_AND = [1, 0, 1, 0, 0, 1, 0, 0]

test_aluControls = test_aluControl_AND
aluControl = circuits.aluControl(test_aluControls)
#aluCtl
out_aluControl = aluControl.getCircuitOutput()
opCode = out_aluControl[0]
cin = out_aluControl[1]
alu_32bit = circuits.ALU_32bit(A, B, cin, opCode)
out_alu_and = alu_32bit.getCircuitOutput()
print out_alu_and, "under signal ", test_aluControls, " for AND"

#testing aluControl for OR, ALUOp is 10, function filed is 100101
test_aluControl_OR = [1, 0, 1, 0, 0, 1, 0, 1]

test_aluControls = test_aluControl_OR
aluControl = circuits.aluControl(test_aluControls)
#aluCtl
out_aluControl = aluControl.getCircuitOutput()
opCode = out_aluControl[0]
cin = out_aluControl[1]
alu_32bit = circuits.ALU_32bit(A, B, cin, opCode)
out_alu_or = alu_32bit.getCircuitOutput()
print out_alu_or, "under signal ", test_aluControls, " for OR"

#testing aluControl for slt, ALUOp is 10, function filed is 101010
test_aluControl_slt = [1, 0, 1, 0, 1, 0, 1, 0]

test_aluControls = test_aluControl_slt
aluControl = circuits.aluControl(test_aluControls)
#aluCtl
out_aluControl = aluControl.getCircuitOutput()
opCode = out_aluControl[0]
cin = out_aluControl[1]
alu_32bit = circuits.ALU_32bit(A, B, cin, opCode)
out_alu_slt = alu_32bit.getCircuitOutput()
print out_alu_slt, "under signal ", test_aluControls, " for slt"

#testing aluControl for LW, SW, ALUOp is 00, function filed is xxxxxx
test_aluControl_LWSW = [0, 0, 1, 1, 1, 0, 0, 0]

test_aluControls = test_aluControl_LWSW
aluControl = circuits.aluControl(test_aluControls)
#aluCtl
out_aluControl = aluControl.getCircuitOutput()
opCode = out_aluControl[0]
cin = out_aluControl[1]
alu_32bit = circuits.ALU_32bit(A, B, cin, opCode)
out_alu_LWSW = alu_32bit.getCircuitOutput()
print out_alu_LWSW, "under signal ", test_aluControls, " for LW and SW"

