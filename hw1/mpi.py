# Save as mpi.py and run.
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank() # index of the current process 
print ("hello from process ", rank)
