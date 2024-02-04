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
    d = 1 # forget
    t = 1

    def __init__(self, initState, P_array, Q_array, R_array):
        self.Xe = initState
        self.Pe = np.diag(P_array)
        self.Q = np.diag(Q_array)
        self.R = np.diag(R_array)
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
        self.K = self.Pp * self.H.T * np.linalg.inv(self.H * self.Pp * self.H.T + self.R)
        print(self.K)

        self.Xe = self.Xp + self.K * (Obs - self.H * self.Xp)
        self.Pe = (numpy.matlib.eye(n=9, M=9) - self.K * self.H) * self.Pe
    
    def AdaptiveUpdate(self, Obs):
        self.t = self.t + 1
        self.d = 1 / self.t
        epsilon = Obs - self.H * self.Xp
        self.R = (1 - self.d) * self.R + self.d * (epsilon * epsilon.T - self.H * self.Pp * self.H.T ) # sage Husa update
        self.K = self.Pp * self.H.T * np.linalg.inv(self.H * self.Pp * self.H.T + self.R.T)
        self.Xe = self.Xp + self.K * epsilon
        self.Pe = (numpy.matlib.eye(n=9, M=9) - self.K * self.H) * self.Pe

    def getState(self):
        return self.Xe
    
    def printRQ(self):
        print(self.R)
        print(self.Q)
