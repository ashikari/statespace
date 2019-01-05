import numpy as np
import numpy.linalg as la

A = np.matrix([[-1, 4],[-3, 2]])
B = np.transpose( np.matrix([0, 2]) )
C = np.matrix([1, 0])

#find the observer poles by finding the tranpose of the observer closed loop equation
#x_dot = Ax+Bu
#y = Cx
#
#Acl_O = (A-K*C) 

#take the transpose
At = A.transpose()
Bt = C.transpose()
c_ability = np.concatenate((Bt,At*Bt),axis = 1)
c_ability_inv = la.inv(c_ability)
en_T = c_ability_inv[-1,:]

#concatenate
P = np.concatenate((en_T,en_T*At), axis = 0)
Pinv = la.inv(P)

#cannonical form
Ap = P*At*Pinv
Bp = P*Bt ## we know this is [0, 1].tranpose() because this is controller cannonical form

#calculate control law in cannonical
Gp = Ap[-1,:] + np.matrix([49, 14]) 

#calculate control law in original state rep
G = Gp*P
K = G.transpose()
Acl_O = A - K*C
[evalues, evectors] = la.eig(Acl_O)

print evalues

