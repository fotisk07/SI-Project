import numpy as np
import Sim as sim
import math
import ticks_utils as tu
from numpy.linalg import inv


ticksTours = 10
velocity = 10
acceleration = 0
startPos = 5
enc = sim.Encoder(ticksTours,velocity,acceleration,startPos)
t = 10
dt = 1
X = np.array([[startPos],
              [velocity]])

X_encoder = np.array([0,0])
error_est_x = 20
error_est_v = 5

# Observation Errors
error_obs_x = 25  # Uncertainty in the measurement
error_obs_v = 6


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
    ticks = enc.getTicks(i)
    X_encoder[0] = tu.ticks_to_dist(ticks,ticksTours)
    X_encoder[1] = tu.ticks_to_v(X_encoder[0],i)
    z = np.c_[X_encoder[0], X_encoder[1]]
    n = len(z[0])
    X = prediction2d(X[0][0], X[1][0], dt, a=0)
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

    # Update Process Covariance Matrix
    P = (np.identity(len(K)) - K.dot(H)).dot(P)

print("Final State:\n",X)
