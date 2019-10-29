import numpy as np


def make_frame(data):
    np.savetxt("Animate/produced_map.txt",data, delimiter=',',newline='\n')
    
            
