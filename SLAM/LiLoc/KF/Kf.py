import numpy as np
from numpy.linalg import inv
from KF import predictionMatrix as pM

class Filter:
    '''
    A filter object that predicts the current state using a Kalma filter algorithm
    Notation:
    State: X := [x,xdot]
    Measurements: M := [xMes, xdotMes]
    Covariance Matrix: P := [[sigmaX , 0], [0, simgaXDot]]
    '''
    def __init__(self,error_obs_x,error_est_x, error_est_xdot, error_obs_xdot,dt=1):
        self.P = pM.covariance2d(error_est_x, error_est_xdot) #Process covariance matrix
        self.dt = dt
        self.A = np.array([[1, dt],
                      [0, 1]])
        self.H = np.identity(2) #formatting matrix
        self.R = pM.covariance2d(error_obs_x, error_obs_xdot) # Error in measurement
        self.S = np.zeros((2,2)) #formatting matrix
        self.K = np.zeros((2,2)) #Kalman gain
        self.Y = np.zeros((2,1)) # For reshaping new data to measuremnt space
        self.XP_fp = np.zeros((2,1))

    def NewState(self, X, M, a):
            n = len(M) #Array size
            X = pM.prediction2d(X[0][0], X[1][0], self.dt, a) #Predict state
            self.XP_fp = X

            # To simplify the problem set off-diagonal terms to 0.
            self.P = np.diag(np.diag(self.A.dot(self.P).dot(self.A.T)))

            # Calculating the Kalman Gain
            self.S = (self.H).dot(self.P).dot(self.H.T) + self.R
            self.K = self.P.dot(self.H).dot(inv(self.S)) #Kalman gain

            # Reshape the new data into the measurement space.
            self.Y = self.H.dot(M).reshape(n, -1)

            # Update the State Matrix
            # Combination of the predicted state, measured values, covariance matrix and Kalman Gain
            X = X + self.K.dot(self.Y - self.H.dot(X))
            # Update Process Covariance Matrix
            self.P = (np.identity(len(self.K)) - self.K.dot(self.H)).dot(self.P)
            return X
