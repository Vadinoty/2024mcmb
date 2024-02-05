import akf
import math
import random
import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt

fail = 0
total = 1000

for iter in range (0, total):
    State = numpy.matlib.mat([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=np.float64).reshape(9, 1)
    P_arr = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], dtype=np.float64)
    Q_arr = np.array([0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001], dtype=np.float64)
    R_arr = np.array([0.01, 0.01, 0.01], dtype=np.float64)
    kf_sub = akf.kalman_filter(initState=State, P_array=P_arr, Q_array=Q_arr, R_array=R_arr)

    search_radius = 40 
    Initial_distance = 1000
    search_speed = 20.0
    seaspeedx = 10.0
    seaspeedy = 10.0
    vx10 = 0.0
    vx20 = 15.0
    vy10 = 0.0
    vy20 = 0.0

    x1 = 0.0
    y1 = 0.0
    x2 = 0.0
    y2 = 0.0
    vx1 = vx10
    vy1 = vy10
    vx2 = vx20
    vy2 = vy20

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
    listx1e = []
    listy1e = []
    listx2 = []
    listy2 = []
    a = 0.3

    while x1*x1+y1*y1 < Initial_distance*Initial_distance:
        # Subs Update
        accx1 = random.gauss((seaspeedx - vx1)/(seaspeedx+vx1), 0.1)
        accy1 = random.gauss((seaspeedy - vy1)/(seaspeedy+vy1), 0.1)
        x1 = x1 + vx1*dt
        y1 = y1 + vy1*dt
        vx1 = vx1 + accx1*dt
        vy1 = vy1 + accy1*dt
        # listx1.append(x1)
        # listy1.append(y1)

        # Estimate
        Obsnoisex = random.gauss(0, 0.1)
        Obsnoisey = random.gauss(0, 0.1)
        Observe = numpy.matlib.mat([[accx1 + Obsnoisex], [accy1 + Obsnoisey], [0.00]], dtype=np.float64)
        kf_sub.Predict(dt)
        kf_sub.Update(Observe)
        cur_state = kf_sub.getState()
        # listx1e.append(cur_state[0, 0])
        # listy1e.append(cur_state[1, 0])

    # After move
    NewState = numpy.matlib.mat([x1, y1, 0, vx1, vx2, 0, 0, 0, 0], dtype=np.float64).reshape(9, 1)
    kf_sub.setState(NewState)
    kf_sub.setP(P_arr)

    i = 0

    while (x2-x1)**2 + (y2-y1)**2 > search_radius * search_radius:
        # Subs Update
        accx1 = random.gauss((seaspeedx - vx1)/(seaspeedx+vx1), 0.1)
        accy1 = random.gauss((seaspeedy - vy1)/(seaspeedy+vy1), 0.1)
        x1 = x1 + vx1*dt
        y1 = y1 + vy1*dt
        vx1 = vx1 + accx1*dt
        vy1 = vy1 + accy1*dt
        # listx1.append(x1)
        # listy1.append(y1)
        # print(vx1)
        # print(vy1)

        # Estimate
        Obsnoisex = random.gauss(0, 0.1)
        Obsnoisey = random.gauss(0, 0.1)
        Observe = numpy.matlib.mat([[accx1 + Obsnoisex], [accy1 + Obsnoisey], [0.00]], dtype=np.float64)
        kf_sub.Predict(dt)
        kf_sub.Update(Observe)
        cur_state = kf_sub.getState()
        xe1 = cur_state[0, 0]
        ye1 = cur_state[1, 0]
        # listx1e.append(xe1)
        # listy1e.append(ye1)

        # search
        vx2 = search_speed * (xe1 - x2) / math.sqrt((xe1 - x2)**2 + (ye1 - y2)**2)
        vy2 = search_speed * (ye1 - y2) / math.sqrt((xe1 - x2)**2 + (ye1 - y2)**2)
        x2 = x2 + vx2*dt
        y2 = y2 + vy2*dt
        # listx2.append(x2)
        # listy2.append(y2)
        i = i + 1

        if(i > 100000): 
            fail = fail + 1
            break 
        # print(i)

    print("["+repr(iter)+"/"+repr(total)+"]: i = "+repr(i))
winrate = 1 - fail/total
print(winrate)


# plt.plot(listx1, listy1)
# plt.plot(listx1e, listy1e)
# plt.plot(listx2, listy2)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Only Subs")
# plt.show()
