from KF import Kf as kalman
from Encoder import Sim
from Encoder import ticks_utils as tu
from KF import plot_utils as plot
import numpy as np
import matplotlib.pyplot as plt

dt=1
t=50
#Prediction erros
error_est_x = 5
error_est_xdot = 50

# Observation Errors
error_obs_x = 5  # Uncertainty in the measurement
error_obs_xdot = 1

filter = kalman.Filter(error_obs_x,error_est_x, error_est_xdot, error_obs_xdot, dt) #Initialize Kf method

ticksTours = 10
startPos = 1
startV = 1
a=0

M = np.array([0,0])
X = np.array([[startPos],
              [startV]])

enc = Sim.Encoder(ticksTours,startV,a,startPos)

#fp stands for "for plotting"
XV_fP = np.zeros((2,t-1)) #True state
XP_fP = np.zeros((2,t-1)) #Predicted state
M_fp = np.zeros((2,t-1))  #Measurements
M_fp[0][-1] = startPos  #Stupid fix DO NOT TOUCH
X_fp = np.zeros((2,t-1))  #State

for i in range(1,t,dt):
    ticks = enc.getTicks(i,noise=True)
    M[0] = tu.ticks_to_dist(ticks,ticksTours,startPos)
    M[1] = tu.ticks_to_v(M[0]-M_fp[0][i-2],dt)

    X  = filter.NewState(X, M, a)

    #Plotting
    M_fp[0][i-1]=M[0]
    M_fp[1][i-1]=M[1]
    XP_fP[0][i-1] = filter.XP_fp[0][0]
    XP_fP[1][i-1] = filter.XP_fp[1][0]
    XV_fP[0][i-1] = enc.distance(i)
    XV_fP[1][i-1] = enc.vel(i)
    X_fp[0][i-1]=X[0]
    X_fp[1][i-1]=X[1]

print("The state matrix is:",X)

plot.plotData(XV_fP[0][:],XP_fP[0][:], M_fp[:][0],X_fp[0][:], t, dt,"Position Inference","Position" , start = startPos)
plot.plotData(XV_fP[1][:],M_fp[1][:], X_fp[:][1],X_fp[1][:], t, dt,"Velocity Inference","Velocity" , start = startV)
plt.show()
