__author__ = "Your name, Yueming Yang"
__Copyright__ =  "Copyright @2016, Mount Holyoke College"


class circuit(object):
	def __init__(self, in1, in2):
		self.in1_ = in1
		self.in2_ = in2

class andgate(circuit):
	def getCircuitOutput(self):
		if self.in1_ == 1 and self.in2_ == 1:
			return 1
		else:
			return 0

class orgate(circuit):
	def getCircuitOutput(self):
		if self.in1_ == 0 and self.in2_ == 0:
			return 0
		else:
			return 1

class notgate(circuit):
	def __init__(self, in1):
		self.in1_ = in1

	def getCircuitOutput(self):
		if self.in1_ == 1:
			return 0
		elif self.in1_ == 0:
			return 1

 #xorgate boolean algebra: Y = A'B+AB'
class xorgate(circuit):
	def getCircuitOutput(self):
		notg0 = notgate(self.in1_)
		out_notg0 = notg0.getCircuitOutput()

		andg0 = andgate(out_notg0, self.in2_)
		out_andg0 = andg0.getCircuitOutput()

		notg1 = notgate(self.in2_)
		out_notg1 = notg1.getCircuitOutput()

		andg1 = andgate(self.in1_, out_notg1)
		out_andg1 = andg1.getCircuitOutput()

		org0 = orgate(out_andg0, out_andg1)
		out_org0 = org0.getCircuitOutput()

		return out_org0

#andgate3 boolean algebra: Y=ABC
class andgate3(circuit):
	def __init__(self, in1, in2, in3):
		self.in1_ = in1
		self.in2_ = in2
		self.in3_ = in3

	def getCircuitOutput(self):
		andg0 = andgate(self.in1_, self.in2_)
		out_andg0 = andg0.getCircuitOutput()

		andg1 = andgate(out_andg0, self.in3_)
		out_andg1 = andg1.getCircuitOutput()

		return out_andg1

#6 inputs andgates
class andgate6(circuit):
	def __init__(self, in1, in2, in3, in4, in5, in6):
		self.in1_ = in1
		self.in2_ = in2
		self.in3_ = in3
		self.in4_ = in4 
		self.in5_ = in5 
		self.in6_ = in6 

	def getCircuitOutput(self):
		andg0 = andgate3(self.in1_, self.in2_, self.in3_)
		out_andg0 = andg0.getCircuitOutput()

		andg1 = andgate3(self.in4_, self.in5_, self.in6_)
		out_andg1 = andg1.getCircuitOutput()

		andg2 = andgate(out_andg0, out_andg1)
		out_andg2 = andg2.getCircuitOutput()

		return out_andg2

class andgate5(circuit):
	def __init__(self, in1, in2, in3, in4, in5):
		self.in1_ = in1
		self.in2_ = in2
		self.in3_ = in3
		self.in4_ = in4 
		self.in5_ = in5 

	def getCircuitOutput(self):
		andg0 = andgate3(self.in1_, self.in2_, self.in3_)
		out_andg0 = andg0.getCircuitOutput()

		andg1 = andgate(self.in4_, self.in5_)
		out_andg1 = andg1.getCircuitOutput()

		andg2 = andgate(out_andg0, out_andg1)
		out_andg2 = andg2.getCircuitOutput()

		return out_andg2

#orgate3 boolean algebra: Y=A+B+C
class orgate3(circuit):
	def __init__(self, in1, in2, in3):
		self.in1_ = in1
		self.in2_ = in2
		self.in3_ = in3

	def getCircuitOutput(self):
		org0 = orgate(self.in1_, self.in2_)
		out_org0 = org0.getCircuitOutput()

		org1 = orgate(out_org0, self.in3_)
		out_org1 = org1.getCircuitOutput()

		return out_org1


#orgate4 boolean algebra: Y=A+B+C+D
class orgate4(circuit):
	def __init__(self, in1, in2, in3, in4):
		self.in1_ = in1
		self.in2_ = in2
		self.in3_ = in3
		self.in4_ = in4

	def getCircuitOutput(self):
		org3_0 = orgate3(self.in1_, self.in2_, self.in3_)
		out_org30 = org3_0.getCircuitOutput()

		org1 = orgate(out_org30, self.in4_)
		out_org1 = org1.getCircuitOutput()

		return out_org1

#2to1 mux implemented by notgate, andgates and orgates
class mux_2to1(circuit):
	def __init__(self, in1, in2, s0):
		self.in1_ = in1
		self.in2_ = in2
		self.s0_ = s0

	def getCircuitOutput(self):
		notg = notgate(self.s0_);
		out_notg = notg.getCircuitOutput()
		andg_1 = andgate(self.in1_, out_notg)
		out_andg_1 = andg_1.getCircuitOutput()
		andg_2 = andgate(self.in2_, self.s0_)
		out_andg_2 = andg_2.getCircuitOutput()
		org = orgate(out_andg_1, out_andg_2)
		out_org = org.getCircuitOutput()

		return out_org


#4to1 mux implemented by 2to1 muxes
class mux_4to1(circuit):
	def __init__(self, in1, in2, in3, in4, s0, s1):
		self.in1_ = in1
		self.in2_ = in2
		self.in3_ = in3
		self.in4_ = in4
		self.s0_ = s0
		self.s1_ = s1

	def getCircuitOutput(self):
		mux21_1 = mux_2to1(self.in1_, self.in2_, self.s1_)
		out_mux21_1 = mux21_1.getCircuitOutput()
		mux21_2 = mux_2to1(self.in3_, self.in4_, self.s1_)
		out_mux21_2 = mux21_2.getCircuitOutput()
		mux21_3 = mux_2to1(out_mux21_1, out_mux21_2, self.s0_)
		out_mux21_3 = mux21_3.getCircuitOutput()

		return out_mux21_3


#fulladder implemented with logic gates
class fulladder(circuit):
	def __init__(self, in1, in2, c0):
		self.in1_ = in1
		self.in2_ = in2 
		self.c0_ = c0 

	def getSum(self):
		#A'
		notg_1 = notgate(self.in1_)
		out_notg_1 = notg_1.getCircuitOutput()
		#B'
		notg_2 = notgate(self.in2_)
		out_notg_2 = notg_2.getCircuitOutput()
		#C'
		notg_3 = notgate(self.c0_)
		out_notg_3 = notg_3.getCircuitOutput()
		#A'BC;
		andg_1 = andgate3(out_notg_1, self.in2_, out_notg_3)
		out_andg_1 = andg_1.getCircuitOutput()
		#AB'C'
		andg_2 = andgate3(self.in1_, out_notg_2, out_notg_3)
		out_andg_2 = andg_2.getCircuitOutput()
		#A'B'C
		andg_3 = andgate3(out_notg_1, out_notg_2, self.c0_)
		out_andg_3 = andg_3.getCircuitOutput()
		#ABC
		andg_4 = andgate3(self.in1_, self.in2_, self.c0_)
		out_andg_4 = andg_4.getCircuitOutput()
		#Y = A'BC' + AB'C' + A'B'C + ABC
		org = orgate4(out_andg_1, out_andg_2, out_andg_3, out_andg_4)
		out_org = org.getCircuitOutput()

		return out_org

	def getCout(self):
		#AB
		andg_1 = andgate(self.in1_, self.in2_)
		out_andg_1 = andg_1.getCircuitOutput()
		#BC
		andg_2 = andgate(self.in2_, self.c0_)
		out_andg_2 = andg_2.getCircuitOutput()
		#AC
		andg_3 = andgate(self.in1_, self.c0_)
		out_andg_3 = andg_3.getCircuitOutput()
		#AB+BC+AC
		org = orgate3(out_andg_1, out_andg_2, out_andg_3)
		out_org = org.getCircuitOutput()

		return out_org



#1 bit ALU implemented with logic gates
class ALU_1bit(object):
	def __init__(self, in1, in2, cin, OpCtrl):
		self.in1_ = in1
		self.in2_ = in2 
		self.cin_ = cin 
		self.ainvert_ = OpCtrl[0]
		self.binvert_ = OpCtrl[1] 
		self.s1_ = OpCtrl[2] 
		self.s0_ = OpCtrl[3]

	def getCircuitOutput(self):
		#2to1 multiplexer for in1
		notg_1 = notgate(self.in1_)
		out_notg_1 = notg_1.getCircuitOutput()
		mux21_1 = mux_2to1(self.in1_, out_notg_1, self.ainvert_)
		out_mux21_1 = mux21_1.getCircuitOutput()
		#2to1 multiplexer for in1
		notg_2 = notgate(self.in2_)
		out_notg_2 = notg_2.getCircuitOutput()
		mux21_2 = mux_2to1(self.in2_, out_notg_2, self.binvert_)
		out_mux21_2 = mux21_2.getCircuitOutput()

		#AND
		andg_01 = andgate(out_mux21_1, out_mux21_2)
		out_andg_01 = andg_01.getCircuitOutput()

		#OR
		org_01 = orgate(out_mux21_1, out_mux21_2)
		out_org_01 = org_01.getCircuitOutput()

		#Addition
		add_01 = fulladder(out_mux21_1, out_mux21_2, self.cin_)
		out_add_01 = add_01.getSum()
		out_cout = add_01.getCout()

		#mux_4to1
		mux41 = mux_4to1(out_andg_01, out_org_01, out_add_01, 0, self.s1_, self.s0_)
		out_mux41 = mux41.getCircuitOutput();

		return out_mux41, out_cout


class aluControl(circuit):

	def __init__(self, signals):
		self.aluOp2_ = signals[0]
		self.aluOp1_ = signals[1]
		self.f5_ = signals[2] 
		self.f4_ = signals[3] 
		self.f3_ = signals[4]  
		self.f2_ = signals[5]  
		self.f1_ = signals[6]  
		self.f0_ = signals[7]  

	#get the four outputs of the circuits
	def getCircuitOutput(self):
		org_01 = orgate(self.f0_, self.f3_)
		out_org01 = org_01.getCircuitOutput()
		andg_01 = andgate(self.aluOp2_, out_org01)
		out_andg01 = andg_01.getCircuitOutput()  #output 0

		notg_01 = notgate(self.aluOp2_)
		out_notg01 = notg_01.getCircuitOutput()
		notg_02 = notgate(self.f2_)
		out_notg02 = notg_02.getCircuitOutput()
		org_02 = orgate(out_notg01, out_notg02)
		out_org02 = org_02.getCircuitOutput() #output 1

		andg_02 = andgate(self.aluOp2_, self.f1_)
		out_andg02 = andg_02.getCircuitOutput()
		org_03 = orgate(out_andg02, self.aluOp1_)
		out_org03 = org_03.getCircuitOutput() #output2

		notg_03 = notgate(self.aluOp1_)
		out_notg03 = notg_03.getCircuitOutput()
		andg_03 = andgate(out_notg03, self.aluOp1_)
		out_andg03 = andg_03.getCircuitOutput() #output3

		outputs = [out_andg03, out_org03, out_org02, out_andg01]
		if outputs[1] == 1:
			cin = 1
		else:
			cin = 0
		return outputs, cin


class ALU_32bit(object):

	def __init__(self, arr01, arr02, cin, signal):
		self.arr01_ = arr01
		self.arr02_ = arr02 
		self.signal_ = signal
		self.cin_ = cin 

	def getCircuitOutput(self):
		#output array
		output = []
		#initial carryin
		cin = self.cin_
		#slt case
		if self.signal_ == [0,1,1,1]:
			subCtrs = [0, 1, 1, 0]
			for counter in range (32, 0, -1):
				add_1bitalu = ALU_1bit(self.arr01_[counter], self.arr02_[counter], cin, subCtrs)
				slt_1bitalu = ALU_1bit(self.arr01_[counter], self.arr02_[counter], cin, self.signal_)
				out_add_1bit = add_1bitalu.getCircuitOutput()[0]
				output.append(slt_1bitalu.getCircuitOutput()[0])
				cin = add_1bitalu.getCircuitOutput()[1]

			output[31] = out_add_1bit
		#other case
		else:
			for counter in range(32, 0, -1):
				alu_1bit = ALU_1bit(self.arr01_[counter], self.arr02_[counter], cin, self.signal_)
				out_alu_1bit = alu_1bit.getCircuitOutput()
				output.append(out_alu_1bit[0])
				cin = out_alu_1bit[1]

			output.reverse()
		return output 


class mainCtrol(circuit):
	def __init__(self, op5, op4, op3, op2, op1, op0):
		self.op5_ = op5 
		self.op4_ = op4 
		self.op3_ = op3 
		self.op2_ = op2 
		self.op1_ = op1 
		self.op0_ = op0 

	def getCircuitOutput(self):
		output = []
		notg0 = notgate(self.op0_)
		out_notop0 = notg0.getCircuitOutput()
		notg1 = notgate(self.op1_)
		out_notop1 = notg1.getCircuitOutput()
		notg2 = notgate(self.op2_)
		out_notop2 = notg2.getCircuitOutput()
		notg3 = notgate(self.op3_)
		out_notop3 = notg3.getCircuitOutput()
		notg4 = notgate(self.op4_)
		out_notop4 = notg4.getCircuitOutput()
		notg5 = notgate(self.op5_)
		out_notop5 = notg5.getCircuitOutput()

		andg6_0 = andgate6(out_notop0, out_notop1, out_notop2, out_notop3, out_notop4, out_notop5)
		out_andg6_0 = andg6_0.getCircuitOutput()
		
		andg6_1 = andgate6(self.op1_, self.op5_, self.op0_, out_notop2, out_notop3, out_notop4)
		out_andg6_1 = andg6_1.getCircuitOutput()

		andg6_2 = andgate6(self.op5_, self.op3_, self.op1_, self.op0_, out_notop2, out_notop4)
		out_andg6_2 = andg6_2.getCircuitOutput()

		andg6_3 = andgate6(self.op2_, out_notop0, out_notop1, out_notop3, out_notop4, out_notop5)
		out_andg6_3 = andg6_3.getCircuitOutput()

		org_0 = orgate(out_andg6_1, out_andg6_2)
		out_org_0 = org_0.getCircuitOutput()        

		org_1 = orgate(out_andg6_0, out_andg6_1)
		out_org_1 = org_1.getCircuitOutput()

		output.append(out_andg6_0)
		output.append(out_org_0)
		output.append(out_andg6_1)
		output.append(out_org_1)
		output.append(out_andg6_1)
		output.append(out_andg6_2)
		output.append(out_andg6_3)
		output.append(out_andg6_0)
		output.append(out_andg6_3)

		return output


class registerFile(circuit):
	def __init__(self, reg_initial_value):
		self.regInitVal_ = reg_initial_value

	def setRegValue(self, o_regDecoder , valueToSet):
		for counter in range(0,32):
			if o_regDecoder[counter] == 1:
				self.regInitVal_[counter] = valueToSet
				break

	def getRegValue(self, o_regDecoder):
		value = self.regInitVal_[0]
		for counter in range(0,32):
			if o_regDecoder[counter] == 1:
				value = self.regInitVal_[counter]
				break
		return value

	def getAllRegValues(self):
		return self.regInitVal_

class decoderReg(circuit):
	def __init__(self, Instr_RegFiled):
		self.in0_ = Instr_RegFiled[0]
		self.in1_ = Instr_RegFiled[1]
		self.in2_ = Instr_RegFiled[2]
		self.in3_ = Instr_RegFiled[3]
		self.in4_ = Instr_RegFiled[4]

	def getCircuitOutput(self):
		output = []
		notg_0 = notgate(self.in0_)
		out_notg_0 = notg_0.getCircuitOutput()
		notg_1 = notgate(self.in1_)
		out_notg_1 = notg_1.getCircuitOutput()
		notg_2 = notgate(self.in2_)
		out_notg_2 = notg_2.getCircuitOutput()
		notg_3 = notgate(self.in3_)
		out_notg_3 = notg_3.getCircuitOutput()
		notg_4 = notgate(self.in4_)
		out_notg_4 = notg_4.getCircuitOutput()

		for input5 in (self.in0_, out_notg_0):
			for input4 in (self.in1_, out_notg_1):
				for input3 in (self.in2_, out_notg_2):
					for input2 in (self.in3_, out_notg_3):
						for input1 in (self.in4_, out_notg_4):
							andg5 = andgate5(input5, input4, input3, input2, input1)
							out_andg5 = andg5.getCircuitOutput()
							output.append(out_andg5)
		output.reverse()
		return output 

#sign extend		
class signExtend(circuit):
	def __init__(self, instru):
		self.instru_ = instru 
	def getCircuitOutput(self):
		if self.instru_[0] == 0:
			list = [0]*16
			o_signExtend = list + self.instru_
		else:
			list = [1]*16
			o_signExtend = list + self.instru_
		return o_signExtend

class Memory(circuit):
	def __init__(self):
		self.memory_ = [[0]*32]*32

	def biToDecConvert(self, binary):
		sum = 0 
		for counter in range(0, 32):
			sum += 2**(31-counter) * binary[counter]
		return sum

	def lw(self, address):
		memAddress = self.biToDecConvert(address)
		return self.memory_[memAddress]


	def sw(self, address, valueToStore):
		memAddress = self.biToDecConvert(address)
		memory[memAddress] = valueToStore

	def getMemory(self):
		return self.memory_

#simple MIPS
class simpleMIPS(circuit):
	def __init__(self, registers):
		self.register_file = registerFile(registers)

	def getCircuitOutput(self, instru):
		#main control
		mainCtrol_ = mainCtrol(instru[0], instru[1], instru[2], instru[3], instru[4], instru[5])
		out_mainCtrol = mainCtrol_.getCircuitOutput()

		RegDst = out_mainCtrol[0]
		ALUSrc = out_mainCtrol[1]
		MemToReg = out_mainCtrol[2]
		RegWrite = out_mainCtrol[3]
		MemRead = out_mainCtrol[4]
		MemWrite = out_mainCtrol[5]
		Branch = out_mainCtrol[7]
		ALUOp1 = out_mainCtrol[7]
		ALUOp0 = out_mainCtrol[8]
		signal_8digit = [ALUOp1, ALUOp0] + instru[26:32]
		
		#get 4 digit operation code
		aluCtrl = aluControl(signal_8digit)
		out_aluCtrl = aluCtrl.getCircuitOutput()


		opctrl = out_aluCtrl[0]
		#get cin for alu-32bit
		cin = out_aluCtrl[1]

		#[25-21]
		rs_5digit = instru[6:11]
		decoderReg_0 = decoderReg(rs_5digit)
		rs = decoderReg_0.getCircuitOutput()
		#[20-16]
		rt_5digit = instru[12:17]
		decoderReg_1 = decoderReg(rt_5digit)
		rt = decoderReg_1.getCircuitOutput()

		#[15-11]
		rd_5digit = instru[18:23]
		for counter in range(18,23):
			rd_5digit.append(instru[counter])
		decoderReg_2 = decoderReg(rd_5digit)
		rd = decoderReg_2.getCircuitOutput()

		#[15-0]
		immediate_16digit = instru[18:32]
		signExt = signExtend(immediate_16digit)
		immediate = signExt.getCircuitOutput()

		arr1 = self.register_file.getRegValue(rs)
		arr2 = self.register_file.getRegValue(rt)

		if ALUSrc == 0:
			o_aluSrc = arr2
		else:
			o_aluSrc = immediate
		
		
		alu_32bit = ALU_32bit(arr1, o_aluSrc, cin, opctrl)
		out_alu_32bit = alu_32bit.getCircuitOutput()

		if RegDst == 0:
			o_regDst = rt
		else:
			o_regDst = rd 

		memory = Memory()
		
		o_lw = memory.lw(out_alu_32bit)
		if MemWrite == 1:
			memory.sw(out_alu_32bit, arr2)

		if MemToReg == 0:
			o_memToReg = o_lw
		else:
			o_memToReg = out_alu_32bit

		if RegWrite == 1:
			self.register_file.setRegValue(rd, o_memToReg)

		o_memory = memory.getMemory()
		return self.register_file, o_memory, out_alu_32bit



