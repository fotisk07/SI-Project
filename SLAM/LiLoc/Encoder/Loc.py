import numpy as np
import Sim as sim
import math
import ticks_utils as tu
from numpy.linalg import inv
import plot_utils as plot
import matplotlib.pyplot as plt

ticksTours = 10
velocity = 1
acceleration = 0
startPos = 20
enc = sim.Encoder(ticksTours,velocity,acceleration,startPos)
t = 100
dt = 1
X = np.array([[startPos],
              [velocity]])

trueStateP = np.zeros((2,t-1))
predictedStateP = np.zeros((2,t-1))
measuredStateP = np.zeros((2,t-1))
KFstate = np.zeros((2,t-1))

X_encoder = np.array([0,0])

#Estimation erros
error_est_x = 5
error_est_v = 1

# Observation Errors
error_obs_x = 15  # Uncertainty in the measurement
error_obs_v = 50


def prediction2d(x, v, t, a):
    A = np.array([[1, t],
                  [0, 1]])
    X = np.array([[x],
                  [v]])
    B = np.array([[0.5 * t ** 2],
                  [t]])
    X_prime = A.dot(X) + B.dot(a)
    return X_prime

def covariance2d(sigma1, sigma2):
    cov1_2 = sigma1 * sigma2
    cov2_1 = sigma2 * sigma1
    cov_matrix = np.array([[sigma1 ** 2, cov1_2],
                           [cov2_1, sigma2 ** 2]])
    return np.diag(np.diag(cov_matrix))

# Initial Estimation Covariance Matrix
P = covariance2d(error_est_x, error_est_v)
A = np.array([[1, dt],
              [0, 1]])

for i in range(1,t,dt):
    #Plotting utils
    trueStateP[0][i-1] = enc.distance(i)
    trueStateP[1][i-1] = enc.vel(trueStateP[0][i-1], i)

    ticks = enc.getTicks(i,noise=True)
    X_encoder[0] = tu.ticks_to_dist(ticks,ticksTours,startPos)
    X_encoder[1] = tu.ticks_to_v(X_encoder[0],i,startPos)
    measuredStateP[0][i-1]=X_encoder[0]
    measuredStateP[1][i-1]=X_encoder[1]
    n = len(X_encoder)

    X = prediction2d(X[0][0], X[1][0], dt, a=0)
    predictedStateP[0][i-1] = X[0][0]
    predictedStateP[1][i-1] = X[1][0]
    # To simplify the problem, professor
    # set off-diagonal terms to 0.
    P = np.diag(np.diag(A.dot(P).dot(A.T)))

    # Calculating the Kalman Gain
    H = np.identity(n)
    R = covariance2d(error_obs_x, error_obs_v)
    S = H.dot(P).dot(H.T) + R
    K = P.dot(H).dot(inv(S))

    # Reshape the new data into the measurement space.
    Y = H.dot(X_encoder).reshape(n, -1)

    # Update the State Matrix
    # Combination of the predicted state, measured values, covariance matrix and Kalman Gain
    X = X + K.dot(Y - H.dot(X))
    KFstate[0][i-1]=X[0]
    KFstate[1][i-1]=X[1]
    # Update Process Covariance Matrix
    P = (np.identity(len(K)) - K.dot(H)).dot(P)

print("Final State:\n",X)
print(measuredStateP)
plot.plotData(trueStateP[0][:],predictedStateP[0][:], measuredStateP[:][0],KFstate[0][:], t, dt,"Position Inference","Position" , start = startPos)
plot.plotData(trueStateP[1][:],predictedStateP[1][:], measuredStateP[:][1],KFstate[1][:], t, dt,"Velocity Inference","Velocity" , start = velocity)
plt.show()
