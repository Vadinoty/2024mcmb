import numpy.matlib
import numpy as np


# State Definition: 9 dims, positionXYZ, VelocityXYZ, AccXYZ
# x, y, z, vx, vy, vz, ax, ay, az, 

class kalman_filter:
    Xe = numpy.matlib.zeros(shape=(9, 1), dtype=np.float64) # Estimate
    Xp = numpy.matlib.zeros(shape=(9, 1), dtype=np.float64) # Predict
    F = numpy.matlib.zeros(shape=(9, 9), dtype=np.float64)
    H = numpy.matlib.zeros(shape=(3, 9), dtype=np.float64)
    Pe = numpy.matlib.zeros(shape=(9, 9), dtype=np.float64)
    Pp = numpy.matlib.zeros(shape=(9, 9), dtype=np.float64)
    Q = numpy.matlib.zeros(shape=(9, 9), dtype=np.float64)
    R = numpy.matlib.zeros(shape=(3, 3), dtype=np.float64)
    K = numpy.matlib.zeros(shape=(9, 3), dtype=np.float64)

    def __init__(self, initState, P_array, Q_array, R_array):
        self.Xe = initState
        self.Pe = P_array.diagonal
        self.Q = Q_array.diagonal
        self.R = R_array.diagonal
        self.F = numpy.matlib.eye(n=9, M=9)
        self.H = numpy.matlib.mat([[0, 0, 0, 0, 0, 0, 1, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 1]], dtype=np.float64)
        
    def Predict(self, dT):
        self.F = numpy.matlib.mat([[1, 0, 0, dT, 0, 0, 0, 0, 0],
                              [0, 1, 0, 0, dT, 0, 0, 0, 0],
                              [0, 0, 1, 0, 0, dT, 0, 0, 0],
                              [0, 0, 0, 1, 0, 0, dT, 0, 0],
                              [0, 0, 0, 0, 1, 0, 0, dT, 0],
                              [0, 0, 0, 0, 0, 1, 0, 0, dT],
                              [0, 0, 0, 0, 0, 0, 1, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 1]])
        self.Xp = self.F * self.Xe # predict
        self.Pp = self.F * self.Pe * self.F.T + self.Q

    def Update(self, Obs):
        self.K = self.Pp * self.H.T / (self.H * self.Pp * self.H.T + self.R.T)
        self.Xp = self.Xe + self.K * (Obs - self.H * self.Xe)
        self.Pe = (numpy.matlib.eye(n=9, M=9) - self.K * self.H) * self.Pe
