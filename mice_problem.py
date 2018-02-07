"""Numerical solution for mice problem
   Newobie approach
   Utilize 2.7 version of Python
"""
from math import sqrt,atan,pi,cos,sin
import numpy as np
from numpy import float32
import matplotlib.pyplot as plt
import matplotlib.animation as animation

a=float32(raw_input('Enter length of the square: '))
v=float32(raw_input('Enter the velocity of the mice: '))
a=a*sqrt(2)
crash=1e-7 #Criteria for crash
I=1e-3 #Time interval for numerical calculation
p1=[-0.5*a,0]
p2=[0,-0.5*a]
p3=[0.5*a,0]
p4=[0,0.5*a]
#p1=[0,0]
#p2=[a,0]
#p3=[a,a]
#p4=[0,a]
P=[p1,p2,p3,p4]
time_cnt=0
PLOTX=[]
PLOTY=[]
P_trjc=[]
Pt=[]
while abs(P[0][0]-P[1][0])>crash and\
      abs(P[0][1]-P[1][1])>crash:
    k=(P[0][1]-P[1][1])/(P[0][0]-P[1][0])
    time_cnt+=I
    Ptrn=[]
    for i in range(len(P)):
	alfai=atan(k)+i*pi/2
	vx=v*cos(alfai)
	vy=v*sin(alfai)
	P[i][0]=P[i][0]+vx*I
	P[i][1]=P[i][1]+vy*I
	Ptrn.append([P[i][0],P[i][1]])
    Pt.append(time_cnt)
    P_trjc.append(Ptrn)
    PLOTX.append(time_cnt)
    PLOTY.append(sqrt((P[0][0]-P[1][0])**2 + (P[0][1]-P[1][1])**2))
    #print 'Rastojanje izmedju 1. i 2. misa je %.5f'\
    #% sqrt((P[0][0]-P[1][0])**2 + (P[0][1]-P[1][1])**2)
    #print 'Vreme proteklo do sudara je %.3f' % time_cnt
    #print
#print time_cnt

Pt1=np.array(Pt)
Ptrjc1=np.array(P_trjc)

def update_plot(i,fig,scat):
    scat.set_offsets((Ptrjc1[i]))
     
    return scat,

fig = plt.figure()

x = [-0.5*a,0,0.5*a,0]
y = [0,-0.5*a,0,0.5*a]
ax=fig.add_subplot(111)

scat = plt.scatter(x,y,c=x)

anim = animation.FuncAnimation(fig,update_plot,fargs=(fig,scat),frames=len(Pt1),interval= 1)

plt.show()
#print PLOTX,PLOTY
#plt.plot(PLOTX,PLOTY)
#plt.show()

