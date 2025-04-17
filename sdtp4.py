from time import sleep
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
TAG = 99

if rank == 0:
    sclib = True
    waiting_list = []

    while True:
        status = MPI.Status()
        msg = comm.recv(source=MPI.ANY_SOURCE, status=status)
        src = status.Get_source()
        print("src:", src)
        if msg == "demande":
            if sclib:
                comm.send("authorized", dest=src)
                sclib = False
            else:
                waiting_list.append(src)

        elif msg == "liberer":
            if waiting_list:
                n_process = waiting_list.pop(0)
                comm.send("authorized", dest=n_process)
            else:
                sclib = True
else:
    while True:
        comm.send("demande", dest=0)
        response = comm.recv(source=0)
        print(f"{rank} received: {response}")
        if response == "authorized":
            sleep(2)
            comm.send("liberer", dest=0)
