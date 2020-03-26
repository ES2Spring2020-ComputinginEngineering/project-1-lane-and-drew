import numpy as np
import matplotlib.pyplot as plt 

lengths=np.array([.71,.61,.51,.41,.31]) #array of pendulum lengths
time = np.linspace(0,10,10000) #list of every number 1-10

def init(a,b): #function that initializes the pendulum based on length and theta
    length = lengths[a]
    postheta = np.pi/b
    veltheta = 0
    acctheta = 0
    return postheta, veltheta, acctheta, length #returns initial values

def update_system(pos,vel,acc,length): #takes in position, velocity, acceleration, and length
    dt = (10/10000) #dt is the change in time between iterations and there are 10,000 steps in time for values between 0 and 10.
    posNext = pos+vel*dt #eulers method to find position
    velNext = vel+acc*dt #eulers method to find velocity
    accNext = -9.81*np.sin(pos)/length #eulers method to find acceleration using calculations explained in the report
    return posNext, velNext, accNext, length #return the values

def plot(posNext,velNext,accNext,length): #takes in four values
    posx = np.zeros((1,1)) #creates 4 empty 1d arrays
    velx = np.zeros((1,1))
    accx = np.zeros((1,1))
    t = np.zeros((1,1))
    i = 0
    while i < len(time): #for every value in time array
        a = update_system(posNext, velNext, accNext, length) #create a 1d array of each value returned by update system
        posNext = a[0] #position = the first value in a
        velNext = a[1] #vel = second value in a
        accNext = a[2] #acc = third value in a
        posx = np.append(posx,length*np.sin(posNext)) #append the cartisean x value (see report for calculations)
        velx = np.append(velx,length*velNext*np.cos(posNext))#append the cartisean vel value (see report for calculations)
        accx = np.append(accx,length*(-np.sin(posNext)*(velNext**2)+np.cos(posNext)*accNext)) #append the cartisean acc value (see report for calculations)
        t = np.append(t,time[i]) #append time value
        i += 1 #repeat for the next value in time
    prev = 0 #counter
    for i in range(0,len(posx)-1): #for every index of posx -1
        if(posx[i]<0 and posx[i+1]>0): #if the current x value is negative and the next is positive
            period = time[i] - prev #the period is equal to the current time - the time when this last occurred
            prev = time[i] #set the time this last occurred to now
    print("Pendulum period " + str(period)) #print the period
            
    plt.xlabel("Time (seconds)")
    plt.ylabel("X position (meters)")
    plt.title("Pendulum Length " + str(length))
    plt.plot(t,posx) #plot x position vs time
    plt.show()
    
    plt.xlabel("Time (seconds)")
    plt.ylabel("X velocity (meters/second)")
    plt.title("Pendulum Length " + str(length))
    plt.plot(t,velx) #plot velocity vs time
    plt.show()
   
    plt.xlabel("Time (seconds)")
    plt.ylabel("X acceleration (meters/second^2)")
    plt.title("Pendulum Length " + str(length))
    plt.plot(t,accx) #plot acceleration vs time
    plt.show()
 
length71 = init(0,10) #length = first value in lengths, theta = pi/10
plot(length71[0],length71[1],length71[2],length71[3]) #plot
length71 = init(0,3/2) #repeat with theta = 2pi/3
plot(length71[0],length71[1],length71[2],length71[3])
                        #repeat with all indexes in lengths array
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
