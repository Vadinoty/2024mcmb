import numpy as py
import random
import matplotlib.pyplot as plt

# model: subs
# x = x + vxdt
# y = y + vydt
# vx = vx + randomx
# vy = 0 + randomy
# Supposed in a small area, the flow goes mainly one way

# model: search boat
# x = x + vxdt
# y = y + vydt
# vx = vx * randomD(D is 0.8 to 1.2)
# vy = 0 + randomy
# suppose that flows has no effect on search boat

fail = 0
total_time = 1000

for iter in range(0,total_time):
    # gauss noise
    mux = 0
    muy = 0
    sgx = 3
    sgy = 3
    search_radius = 40 
    Initial_distance = 1000
    search_sigmay = 10

    listx1 = []
    listx2 = []
    listy1 = []
    listy2 = []

    # subs
    x1 = 0.0
    y1 = 0.0
    vx10 = 10.0 # m/s
    vx1 = 0.0
    vy1 = 0.0
    nx1 = random.gauss(mux, sgx)
    ny1 = random.gauss(muy, sgy)
    # listx1.append(x1)
    # listy1.append(y1)

    # search boat
    x2 = 0.0
    y2 = 0.0
    vx20 = 15.0 # m/s
    vx2 = 0.0
    vy2 = 0.0
    randomD = random.uniform(-0.5, 0.5)
    ny2 = random.gauss(muy, search_sigmay)
    # listx2.append(x2)
    # listy2.append(y2)

    # Time interval
    dt = 0.1 #s
    i = 0

    while x1*x1+y1*y1<Initial_distance*Initial_distance:
        nx1 = random.gauss(mux, sgx)
        ny1 = random.gauss(muy, sgy)
        x1 = x1 + vx1*dt
        y1 = y1 + vy1*dt
        vx1 = vx10 + nx1
        vy1 = ny1
        # listx1.append(x1)
        # listy1.append(y1)

    while (x2-x1)**2 + (y2-y1)**2 > search_radius * search_radius: # when goes into 100m, subs will be found
        nx1 = random.gauss(mux, sgx)
        ny1 = random.gauss(muy, sgy)
        x1 = x1 + vx1*dt
        y1 = y1 + vy1*dt
        vx1 = vx10 + nx1
        vy1 = ny1
        # listx1.append(x1)
        # listy1.append(y1)

        randomD = random.uniform(0.8, 1.2)
        ny2 = random.gauss(muy, search_sigmay)
        x2 = x2 + vx2*dt
        y2 = y2 + vy2*dt
        vx2 = vx20 + randomD
        vy2 = ny2
        # listx2.append(x2)
        # listy2.append(y2)

        i = i + 1
        if i > 10000: 
            fail = fail + 1
            break # failed

    # plt.plot(listx1, listy1, label="Subs")
    # plt.plot(listx2, listy2, label="Search")
    # print("i=",i)
    # print("vx1=", vx1)
    # print("vy1=", vy1)

    # plt.title("Subs")
    # plt.xlabel("x")
    # plt.ylabel("y")

    # plt.show()

winrate = (total_time-fail)/total_time
print(winrate)


