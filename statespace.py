import numpy as np
import numpy.linalg as la


class ss_sys():
	def __init__(self, A,B,C, D=None):
		self.A = A
		self.B = B
		self.C = C
		self.D = D

	def controlM(self):
		A_size = np.shape(A)
		self.ctrb = self.B

		for i in range(1,A_size[0]):
			self.ctrb = np.concatenate((self.ctrb, (self.A**i)*self.B), axis = 1)
		return self.ctrb

	def observeM(self):
		A_size = np.shape(A)
		self.obsv = self.C

		for i in range(1,A_size[0]):
			self.obsv = np.concatenate((self.obsv, self.C*(self.A**i)), axis = 0)
		return self.obsv



def main():

	#set up the instantiation of a state space system
	A = np.matrix([[-1, 4],[-3, 2]])
	B = np.matrix([[ 0 ], [2]])
	C = np.matrix([[1, 0 ]])

	K = ss_sys(A, B, C) #instatiate a system

	#return the controllability and observability matrices
	K.controlM() 
	K.observeM()
	print K.ctrb
	print "\n"
	print K.obsv


if __name__ == '__main__':
	main()



