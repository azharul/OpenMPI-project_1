import numpy as np

#create a 1000 x 1000 matrix
A = np.arange(0,10000,0.01).reshape((1000,1000))

print A.shape

B = A.T
print B.shape

assert A.shape[1]==B.shape[0]

C = np.zeros((A.shape[0], B.shape[1]))
C = np.dot(A,B)
print C.shape
print 'C',C

D = np.zeros((A.shape[0], B.shape[1]))
for i in range(B.shape[1]):
	D[i,:] = np.dot(A,B[:,i])
print 'D', D

assert C.all()==D.all()
