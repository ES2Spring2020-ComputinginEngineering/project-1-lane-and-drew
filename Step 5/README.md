import numpy as np
import matplotlib.pyplot as plt 

lengths=np.array([.71,.61,.51,.41,.31])
time = np.linspace(0,10,10000)

def init(a,b):
    length = lengths[a]
    postheta = np.pi/b
    veltheta = 0
    acctheta = 0
    return postheta, veltheta, acctheta, length

def update_system(pos,vel,acc,length):
    dt = (10/10000)
    posNext = pos+vel*dt
    velNext = vel+acc*dt
    accNext = -9.81*np.sin(pos)/length
    return posNext, velNext, accNext, length

def plot(posNext,velNext,accNext,length):
    posx = np.zeros((1,1))
    velx = np.zeros((1,1))
    accx = np.zeros((1,1))
    t = np.zeros((1,1))
    i = 0
    while i < len(time):
        a = update_system(posNext, velNext, accNext, length)
        posNext = a[0]
        velNext = a[1]
        accNext = a[2]
        posx = np.append(posx,length*np.sin(posNext))
        velx = np.append(velx,length*velNext*np.cos(posNext))
        accx = np.append(accx,length*(-np.sin(posNext)*(velNext**2)+np.cos(posNext)*accNext))
        t = np.append(t,time[i])
        i += 1
    plt.xlabel("Time (seconds)")
    plt.ylabel("X position (meters)")
    plt.title("Pendulum Length " + str(length))
    plt.plot(t,posx)
    plt.show()
    
    plt.xlabel("Time (seconds)")
    plt.ylabel("X velocity (meters/second)")
    plt.title("Pendulum Length " + str(length))
    plt.plot(t,velx)
    plt.show()
   
    plt.xlabel("Time (seconds)")
    plt.ylabel("X acceleration (meters/second^2)")
    plt.title("Pendulum Length " + str(length))
    plt.plot(t,accx)
    plt.show()
    
length71 = init(0,10)
plot(length71[0],length71[1],length71[2],length71[3])
length71 = init(0,3/2)
plot(length71[0],length71[1],length71[2],length71[3])

length61 = init(1,10)
plot(length61[0],length61[1],length61[2],length61[3])
length61 = init(1,3/2)
plot(length61[0],length61[1],length61[2],length61[3])

length51 = init(2,10)
plot(length51[0],length51[1],length51[2],length51[3])
length51 = init(2,3/2)
plot(length51[0],length51[1],length51[2],length51[3])

length41 = init(3,10)
plot(length41[0],length41[1],length41[2],length41[3])
length41 = init(3,3/2)
plot(length41[0],length41[1],length41[2],length41[3])

length31 = init(4,10)
plot(length31[0],length31[1],length31[2],length31[3])
length31 = init(4,3/2)
plot(length31[0],length31[1],length31[2],length31[3])
