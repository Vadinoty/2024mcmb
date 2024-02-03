import kf
import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt

State = numpy.matlib.mat([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=np.float64).reshape(9, 1)
P_arr = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=np.float64)
Q_arr = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], dtype=np.float64)
R_arr = np.array([0.1, 0.1, 0.1], dtype=np.float64)
kf_sub = kf.kalman_filter(initState=State, P_array=P_arr, Q_array=Q_arr, R_array=R_arr)

Observe = numpy.matlib.mat([[0.11], [0.12], [0.09]], dtype=np.float64)

for i in range (1, 100):
    kf_sub.Predict(dT=0.01)
    kf_sub.Update(Obs=Observe)
    kf_sub.PrintOut()