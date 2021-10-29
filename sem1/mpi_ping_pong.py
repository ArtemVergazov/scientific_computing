# Exercise: Perform the same computation in a "ping-pong" manner:
# one process sums only even terms, the other only odd terms;
# after adding a new term the process sends the current result to the other process.
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD 
rank = comm.Get_rank() 

M = 1000
def getPartialSum(start, end, step=1):
    a = np.arange(start, end, step)
    return np.sum(1. / (a * a))

s = getPartialSum(1 + rank, M, step=2)
evenOrOdd = 'even' if rank else 'odd'
print(f'Process {rank} found partial sum of {evenOrOdd} terms: {s}')

# process 1 sends its partial sum to process 0
if rank == 1:
    comm.send(s, dest=0) 
    
# process 0 receives the partial sum from process 1, adds to its own partial sum
# and outputs the result
elif rank == 0: 
    s_other = comm.recv(source=1)
    s_total = s + s_other
    print('total partial sum =', s_total)
    print('pi_approx =', np.sqrt(6 * s_total))
    
print('Process', rank, 'finished')
