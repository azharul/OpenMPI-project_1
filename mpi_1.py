from mpi4py import MPI
import numpy as np

comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()

A = np.arange(0,10000,0.01).reshape((1000,1000))
B = A.T
split=np.empty((10,100000))
data=np.zeros((100,1000))
if rank==0:
for i in range(size):
temp=A[i*100:i*100+100]
split[i]=temp.reshape((1,100000))
else:
split=None

B=comm.bcast(B,root=0)
split=comm.scatter(split,root=0)

split=split.reshape(100,1000)
data=np.dot(split,B)

comm.Barrier()
data=comm.gather(data,root=0)
print np.linalg.det(A)
print np.linalg.det(B)
print data
