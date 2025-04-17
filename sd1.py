from mpi4py import MPI
import numpy

# exuc cmd : mpiexec -np 4 python3 ./sd1.py
# constants de ce tp:
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
# exo 1
# comm_size = comm.Get_size()
# print("I'm the %d process of %dprocesses " %(rank, comm_size))

# exo2:
TAG = 99
if 0 == rank :
    tab = numpy.arange(1,10,2)
    message = "hello ranko"
    comm.send(tab, dest= 1)
    print(str(rank),'send', tab, 'to 1')
if rank == 1 :
    tok = comm.recv(source=0)
    print(str(rank), 'recieve', tok, 'from 0')
# numpy.empty(3,dtype=int)