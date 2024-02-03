import kf
import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt

State = numpy.matlib.mat([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=np.float64)
P_arr = numpy.matlib.mat([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=np.float64)
Q_arr = numpy.matlib.mat([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], dtype=np.float64)
R_arr = numpy.matlib.mat([0.1, 0.1, 0.1], dtype=np.float64)
kf_sub = kf.kalman_filter(initState=State, P_array=P_arr, Q_array=Q_arr, R_array=R_arr)



