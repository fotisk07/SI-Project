import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
plt.style.use('seaborn')

def plotData(true,predicted,measured,kf,  t, dt, name, yAxis,start=0,):
    graph = plt.figure(name)

    x = np.arange(1,t,dt)
    plt.xlabel("Time")
    plt.ylabel(yAxis)
    plt.plot(0,start,'o',color = "black")

    plt.plot(x, true, color="blue", label="True")
    plt.plot(x, predicted, color="red", label="Predicted")
    plt.plot(x, measured, color="magenta", label="Measured")
    plt.plot(x, kf, color="green", label="KF")
    plt.legend()
    graph.savefig(name+".png")
