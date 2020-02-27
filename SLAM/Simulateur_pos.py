from LeadLoc import Kf as kalman
from LeadSim.Position.Encoder import Sim as encSim
from LeadSim.Position.Encoder import ticks_utils as tu
from LeadSim.Position.Gyroscope import Sim as gyroSim
from LeadLoc import plot_utils as plot
import numpy as np
import matplotlib.pyplot as plt

dt=1
t=21
#Prediction erros
error_est_x = 5
error_est_xdot = 1
# Observation Errors
error_obs_x = 5
error_obs_xdot = 1

filterpos = kalman.Filter(error_obs_x,error_est_x, error_est_xdot, error_obs_xdot, dt) #Initialize Kf method

error_est_theta = 5
error_est_thetadot = 50
# Observation Errors
error_obs_theta = 5
error_obs_thetadot = 1

filterangle = kalman.Filter(error_obs_theta,error_est_theta, error_est_thetadot, error_obs_thetadot, dt)


ticksTours = 10
startPos = 2
startV = 4
a=0
startTheta = 0
startThetadot = 20
thetadotdot = 5

M = np.array([0,0,0,0])
X = np.array([[startPos],
              [startV]])
T = np.array([[startTheta],
               [startThetadot]])

enc = encSim.Encoder(ticksTours,startV,a,startPos)
gyro = gyroSim.Gyro(startTheta,startThetadot,thetadotdot)

#fp stands for "for plotting"
XV_fp = np.zeros((4,t-1)) #True state
XP_fp = np.zeros((4,t-1)) #Predicted state
M_fp = np.zeros((4,t-1))  #Measurements
M_fp[0][-1] = startPos  #Stupid fix DO NOT TOUCH
X_fp = np.zeros((4,t-1))  #State


for i in range(1,t,dt):
    ticks = enc.getTicks(i,noise=True)
    M[0] = tu.ticks_to_dist(ticks,ticksTours,startPos)
    M[1] = tu.ticks_to_v(M[0]-M_fp[0][i-2],dt)
    M[2] = gyro.theta(i,noise=True)
    M[3] = gyro.thetadot(i,noise=True)
    X  = filterpos.NewState(X, M[0:2], a)
    T = filterangle.NewState(T, M[2:4], thetadotdot)
    #Plotting
    M_fp[0][i-1]=M[0]
    M_fp[1][i-1]=M[1]
    M_fp[2][i-1]=M[2]
    M_fp[3][i-1]=M[3]
    XP_fp[0][i-1] = filterpos.XP_fp[0][0]
    XP_fp[1][i-1] = filterpos.XP_fp[1][0]
    XP_fp[2][i-1] = filterangle.XP_fp[0][0]
    XP_fp[3][i-1] = filterangle.XP_fp[1][0]
    XV_fp[0][i-1] = enc.distance(i)
    XV_fp[1][i-1] = enc.vel(i)
    XV_fp[2][i-1] = gyro.theta(i)
    XV_fp[3][i-1] = gyro.thetadot(i)
    X_fp[0][i-1]=X[0]
    X_fp[1][i-1]=X[1]
    X_fp[2][i-1]=T[0]
    X_fp[3][i-1]=T[1]


plot.plotData(XV_fp[0][:],XP_fp[0][:], M_fp[:][0],X_fp[0][:], t, dt,"Position Inference","Position" , start = startPos)
plot.plotData(XV_fp[1][:],XP_fp[1][:], M_fp[:][1],X_fp[1][:], t, dt,"Velocity Inference","Velocity" , start = startV)
plot.plotData(np.fmod(XV_fp[2][:],360), np.fmod(XP_fp[2][:],360), np.fmod(M_fp[:][2],360), np.fmod(X_fp[2][:],360), t, dt,"Angle Inference","Angle" , start = startTheta)
plot.plotData(XV_fp[3][:],XP_fp[3][:], M_fp[:][3],X_fp[3][:], t, dt,"Angular Velocity Inference","Angular Velocity" , start = startThetadot)
plt.show()
