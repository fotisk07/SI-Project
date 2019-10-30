import numpy as np


def make_frame(data):
    np.savetxt("produced_map.txt", data, delimiter=',',newline=',' )
    f = open("produced_map.txt", "r")
    current_map = f.read()
    f.close()
    f = open("Animate/frames.txt", "a+")
    f.write(current_map)
    f.write("$")
    f.close()
