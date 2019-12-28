import numpy as np


def prediction2d(x, xdot, dt, a):
    A = np.array([[1, dt],
                  [0, 1]])
    X = np.array([[x],
                  [xdot]])
    B = np.array([[0.5 * dt ** 2],
                  [dt]])
    X_prime = A.dot(X) + B.dot(a)
    return X_prime

def covariance2d(sigma1, sigma2):
    cov1_2 = sigma1 * sigma2
    cov2_1 = sigma2 * sigma1
    cov_matrix = np.array([[sigma1 ** 2, cov1_2],
                           [cov2_1, sigma2 ** 2]])
    return np.diag(np.diag(cov_matrix))
