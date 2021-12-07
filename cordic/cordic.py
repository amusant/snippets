# Thanks to   https://github.com/cebarnes/cordic/blob/master/cordic.py
# Sumanta: adding plotting functions for cordic rotation
import math
import time
import matplotlib.pyplot as plt
import numpy as np
import sys
def create_tan_table(x):
    tan = {}
    for i in range(x):
        tan[2**(-i)] = math.degrees(math.atan(2**(-i)))
    return tan

def cordic_iteration(angle,n):
    x,y = 1.0/find_An(n),0.0
    z = float(angle)
    str_angle = str(angle)
    tan_table = create_tan_table(2*n)

    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='polar')
    r = np.arange(0, 2, 0.01)
    theta = 2 * np.pi *np.ones(200)
    line,=ax.plot(theta, r, 'r-')
    plotangle=0
    theta = (np.pi/180)*plotangle*np.ones(200)
    line.set_xdata(theta)
    fig.canvas.draw()
    fig.canvas.flush_events()
    for i in range(n+1):
        time.sleep(1)
        if z < 0:
            di = -1.0
        else:
            di = +1.0
        newx = x - (y * di * 2.0**(-i)) 
        newy = y + (x * di * 2.0**(-i))
        x = newx
        y = newy
        z = z - (di * tan_table[2.0**(-i)])
        print("Z="+str(z)+": "+str(di * tan_table[2.0**(-i)]))
        plotangle=angle-di*z
        theta = (np.pi/180)*plotangle*np.ones(200)
        line.set_xdata(theta)
        fig.canvas.draw()
        #fig.canvas.flush_events()
    print("cos(angle) = "  + str(x)) 
    print("sin(angle) = "  + str(y))  
    f = math.degrees(x)
    g = math.degrees(y)

    return f,g

def find_angle(t):

    x = t[0]
    y = t[1]
    return math.degrees(math.atan(y/x))


def find_An(n):
    An = math.sqrt(2)
    for i in range(1,n):
        An = An * math.sqrt(1 + 2**(-2*i))
    return An

def main():
    t = cordic_iteration(float(sys.argv[1]),10)
    print ("\nangle rotated = ", find_angle(t))

if __name__ == '__main__':
    main()
