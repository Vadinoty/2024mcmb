import akf
import math
import random
import numpy as np
from scipy.optimize import curve_fit 
import numpy.matlib
import matplotlib.pyplot as plt

State = numpy.matlib.mat([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=np.float64).reshape(9, 1)
P_arr = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], dtype=np.float64)
Q_arr = np.array([0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001], dtype=np.float64)
R_arr = np.array([0.01, 0.01, 0.01], dtype=np.float64)
kf_sub1 = akf.kalman_filter(initState=State, P_array=P_arr, Q_array=Q_arr, R_array=R_arr)
kf_sub2 = akf.kalman_filter(initState=State, P_array=P_arr, Q_array=Q_arr, R_array=R_arr)

search_radius = 40 
Initial_distance = 1000
search_speed = 20.0
seaspeedx = 10.0
seaspeedy = 10.0

found1 = 0
found2 = 0

vx10 = 10.0
vy10 = 10.0

vx20 = 10.0
vy20 = 10.0

vx00 = 0.0
vy00 = 0.0

x1 = 0.0
y1 = 1000.0

x2 = 0.0
y2 = -1000.0

x0 = 1.0
y0 = 1.0

vx1 = vx10
vy1 = vy10

vx2 = vx20
vy2 = vy20

vx0 = vx00
vy0 = vy00

accx1 = 5.0
accy1 = 3.0

accnoisex = 0.0
accnoisey = 0.0

vnoisey = 0.00

Obsnoisex = 0.0
Obsnoisey = 0.0

dt = 0.01
listx1 = []
listy1 = []
listx2 = []
listy2 = []
listx1e = []
listy1e = []
listx2e = []
listy2e = []
listx0 = []
listy0 = []
a = 0.3

# while x1*x1+y1*y1 < Initial_distance*Initial_distance or x2*x2+y2*y2 < Initial_distance*Initial_distance:
#     # Subs1 Update
#     accx1 = random.gauss((seaspeedx - vx1)/(seaspeedx+vx1), 0.1)
#     accy1 = random.gauss((seaspeedy - vy1)/(seaspeedy+vy1), 0.1)
#     x1 = x1 + vx1*dt
#     y1 = y1 + vy1*dt
#     vx1 = vx1 + accx1*dt
#     vy1 = vy1 + accy1*dt
#     listx1.append(x1)
#     listy1.append(y1)

#     # Subs2 Update
#     accx2 = random.gauss((seaspeedx - vx2)/(seaspeedx+vx2), 0.1)
#     accy2 = random.gauss(-(seaspeedy - vy2)/(seaspeedy+vy2), 0.1)
#     x2 = x2 + vx2*dt
#     y2 = y2 + vy2*dt
#     vx2 = vx2 + accx2*dt
#     vy2 = vy2 + accy2*dt
#     listx2.append(x2)
#     listy2.append(y2)

#     # Estimate
#     Obsnoisex = random.gauss(0, 0.1)
#     Obsnoisey = random.gauss(0, 0.1)
#     Observe = numpy.matlib.mat([[accx1 + Obsnoisex], [accy1 + Obsnoisey], [0.00]], dtype=np.float64)
#     kf_sub1.Predict(dt)
#     kf_sub1.Update(Observe)
#     cur_state1 = kf_sub1.getState()

#     Obsnoisex = random.gauss(0, 0.1)
#     Obsnoisey = random.gauss(0, 0.1)
#     Observe = numpy.matlib.mat([[accx2 + Obsnoisex], [accy2 + Obsnoisey], [0.00]], dtype=np.float64)
#     kf_sub2.Predict(dt)
#     kf_sub2.Update(Observe)
#     cur_state2 = kf_sub2.getState()

# After move
NewState1 = numpy.matlib.mat([x1, y1, 0, vx1, vy1, 0, 0, 0, 0], dtype=np.float64).reshape(9, 1)
kf_sub1.setState(NewState1)
kf_sub1.setP(P_arr)
print(NewState1)

cur_state = kf_sub1.getState()
ye = cur_state[1, 0]
print(ye)

NewState2 = numpy.matlib.mat([x2, y2, 0, vx2, vy2, 0, 0, 0, 0], dtype=np.float64).reshape(9, 1)
kf_sub2.setState(NewState2)
kf_sub2.setP(P_arr)

i = 0

while found1 == 0 or found2 == 0:
    # Subs Update
    accx1 = random.gauss((seaspeedx - vx1)/(seaspeedx+vx1)/1000, 0.1)
    accy1 = random.gauss((seaspeedy - vy1)/(seaspeedy+vy1)/1000, 0.1)
    x1 = x1 + vx1*dt
    y1 = y1 + vy1*dt
    vx1 = vx1 + accx1*dt
    vy1 = vy1 + accy1*dt
    listx1.append(x1)
    listy1.append(y1)

    accx2 = random.gauss((seaspeedx - vx2)/(seaspeedx+vx2)/1000, 0.1)
    accy2 = random.gauss((seaspeedy - vy2)/(seaspeedy+vy2)/1000, 0.1)
    x2 = x2 + vx2*dt
    y2 = y2 + vy2*dt
    vx2 = vx2 + accx2*dt
    vy2 = vy2 + accy2*dt
    listx2.append(x2)
    listy2.append(y2)


    # Estimate
    Obsnoisex = random.gauss(0, 0.1)
    Obsnoisey = random.gauss(0, 0.1)
    Observe = numpy.matlib.mat([[accx1 + Obsnoisex], [accy1 + Obsnoisey], [0.00]], dtype=np.float64)
    kf_sub1.Predict(dt)
    kf_sub1.Update(Observe)
    cur_state1 = kf_sub1.getState()
    xe1 = cur_state1[0, 0]
    ye1 = cur_state1[1, 0]
    listx1e.append(xe1)
    listy1e.append(ye1)
    # print(ye1)


    Obsnoisex = random.gauss(0, 0.1)
    Obsnoisey = random.gauss(0, 0.1)
    Observe = numpy.matlib.mat([[accx2 + Obsnoisex], [accy2 + Obsnoisey], [0.00]], dtype=np.float64)
    kf_sub2.Predict(dt)
    kf_sub2.Update(Observe)
    cur_state2 = kf_sub2.getState()
    xe2 = cur_state2[0, 0]
    ye2 = cur_state2[1, 0]
    listx2e.append(xe2)
    listy2e.append(ye2)

    # print(x0)
    # print(y0)

    # search
    if found1 == 0 and found2 == 0:
        if (xe1 - x0)**2 + (ye1 - y0)**2 <= (xe2 - x0)**2 + (ye2 - y0)**2:
            vx0 = search_speed * (xe1 - x0) / math.sqrt((xe1 - x0)**2 + (ye1 - y0)**2)
            vy0 = search_speed * (ye1 - y0) / math.sqrt((xe1 - x0)**2 + (ye1 - y0)**2)
        else:
            vx0 = search_speed * (xe2 - x0) / math.sqrt((xe2 - x0)**2 + (ye2 - y0)**2)
            vy0 = search_speed * (ye2 - y0) / math.sqrt((xe2 - x0)**2 + (ye2 - y0)**2)
    elif found1 == 1:
        vx0 = search_speed * (xe2 - x0) / math.sqrt((xe2 - x0)**2 + (ye2 - y0)**2)  
        vy0 = search_speed * (ye2 - y0) / math.sqrt((xe2 - x0)**2 + (ye2 - y0)**2)
    else :
        vx0 = search_speed * (xe1 - x0) / math.sqrt((xe1 - x0)**2 + (ye1 - y0)**2)
        vy0 = search_speed * (ye1 - y0) / math.sqrt((xe1 - x0)**2 + (ye1 - y0)**2)

    x0 = x0 + vx0*dt
    y0 = y0 + vy0*dt
    listx0.append(x0)
    listy0.append(y0)

    i = i + 1

    if (x0-x1)**2 + (y0-y1)**2 < search_radius * search_radius :
        found1 = 1
    if (x0-x2)**2 + (y0-y2)**2 < search_radius * search_radius :
        found2 = 1
    if(i > 100000): 
        break 

plt.plot(listx0, listy0, label="Search")
plt.plot(listx1, listy1, label="Subs1")
plt.plot(listx1e, listy1e, label="Subs1e")
plt.plot(listx2, listy2, label="Subs2")
plt.plot(listx2e, listy2e, label="Subs2e")
print("i=",i)

plt.title("Subs")
plt.xlabel("x")
plt.ylabel("y")

plt.show()
