import kf
import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt

State = numpy.matlib.mat([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=np.float64).reshape(9, 1)
P_arr = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=np.float64)
Q_arr = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], dtype=np.float64)
R_arr = np.array([0.1, 0.1, 0.1], dtype=np.float64)
kf_sub = kf.kalman_filter(initState=State, P_array=P_arr, Q_array=Q_arr, R_array=R_arr)

noise = np.round(np.random.normal(0, 0.1, 100), 2)
noise_matx = np.array(noise)
noise = np.round(np.random.normal(0, 0.1, 100), 2)
noise_maty = np.array(noise)
noise = np.round(np.random.normal(0, 0.1, 100), 2)
noise_matz = np.array(noise)

# Creating figure
fig = plt.figure(figsize=(10, 7))
ax = plt.axes(projection="3d")

Observe = numpy.matlib.mat([[0.10], [0.10], [0.10]], dtype=np.float64)
for i in range (1, 50):
    noiseObs = numpy.matlib.mat([[noise_matx[i]], [noise_maty[i]], [noise_matz[i]]], dtype=np.float64)
    kf_sub.Predict(dT=0.01)
    kf_sub.Update(Obs=Observe+noiseObs)
    cur_state = kf_sub.getState()
    ax.scatter3D(cur_state[0], cur_state[1], cur_state[2], color="green")

Observe = numpy.matlib.mat([[-0.10], [-0.20], [0.00]], dtype=np.float64)
for i in range (50, 100):
    noiseObs = numpy.matlib.mat([[noise_matx[i]], [noise_maty[i]], [noise_matz[i]]], dtype=np.float64)
    kf_sub.Predict(dT=0.01)
    kf_sub.Update(Obs=Observe+noiseObs)
    cur_state = kf_sub.getState()
    ax.scatter3D(cur_state[0], cur_state[1], cur_state[2], color="green")

plt.title("XYZ")
# show plot
plt.show()
