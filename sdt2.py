from mpi4py import MPI
import time,numpy

# constants de ce tp:
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
data = numpy.zeros(3,dtype=int)
data2= numpy.empty([size,3],dtype=int)
sndata = numpy.full(3,rank)
resdata = None
# exo2: one2one
# if rank == 0 :
#     data= numpy.arange(1,10,3)
# print(f"{rank}: sent content : {data}")
# data= comm.bcast(data, root=0)
# print(f"{rank}: recieved data: {data}")

# exo3:one2*
# if rank ==0:
#     data2 = numpy.arange(size*3).reshape((size,3))
#     print(f"sent: {data2}")
# received = numpy.zeros(3,dtype=int)
# comm.Scatter(data2,received,root=0)
# print(f"received: {received}")

# exo4:*2one
# if rank == 0:
#     resdata = numpy.full(size *3,rank).reshape((size,3))
# print(f'{rank}: received: {resdata}')
# comm.Gather(sndata,resdata,root=0)
# if rank ==0:
#     print(f'{rank}: after receiving: {resdata}')
# exo1 :
# if rank == 0 :
    # Start_time = time.time()
    # time.sleep(2)
# if rank == 1:
#     time.sleep(3)
# if rank == 2 :
#     time.sleep(5)
# comm.barrier()
# if rank == 0:
#     end_time = time.time()
#     elaptime = end_time - Start_time
#     print(elaptime)

# exo5: *2*:
# line = numpy.full(size,rank)
# table = numpy.zeros((size,size),dtype=int)
# print(f'{rank}:line:{line}')
# print(f'{rank}:table:{table}')
# comm.Allgather([line,MPI.INT] , [table,MPI.INT])
# print(f'{rank}:after:{table}')

# exo de test:
