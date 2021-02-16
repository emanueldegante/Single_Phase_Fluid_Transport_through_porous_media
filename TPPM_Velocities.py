# -*- coding: utf-8 -*-
"""
Created on Wed May 27 20:07:10 2020

@author: Emanuel
"""

import numpy as np
import seaborn as sns; sns.set()


po=.25    #porosity
kx=250    #Permeability in X - mD
ky=150    #Permeability in Y - mD
h=30      #payzone ft
rw=.25    #ft
qw=200    #stb/day
Y=35      #API
p=(145/(Y+131.5))
u=3       #cp
p_ext=3000 #psia
Bo=1.2    #Bbl/STB
x=4000   #ft
y=2500   #ft
Nx=40
Ny=25
p_ini=1500
Bx=x/Nx
By=y/Ny
B=((qw*u)/(4*kx*p*h))*(Bx/By)
alpha=(kx/ky)*((Bx/By)**2)



P=np.zeros((Ny,Nx))

for i in range(Nx):
    P[0,i]=p_ext
    for j in range(Ny):
        P[j,Nx-1]=p_ext
#==================================Initial Conditions

for i in range(0,Nx-1):
    for j in range(1,Ny):
        P[j,i]=p_ini

counter=0
while counter<300:
    
    P[Ny-1,0]=(P[Ny-1,1]+(B*P[Ny-2,0])-alpha)/(1+B)  #=================Corner Block
    
    for j in range(Ny-2,0,-1):
        P[j,0]=(P[j,1]+(B*P[j-1,0])+(B*P[j+1,0]))/(1+(2*B))#=============West
    
    for i in range(1,Nx-1):
        P[Ny-1,i]=(P[Ny-1,i+1]+(B*P[Ny-2,i])+(P[Ny-1,i-1]))/(2+B) #========South    
    
    for j in range(Ny-2,0,-1):
        for i in range(1,Nx-1):
            P[j,i]=(P[j,i+1]+(B*P[j-1,i])+P[j,i-1]+(B*P[j+1,i]))/(2*(1+B))#====interior
        
    counter+=1
    
    
    
ax = sns.heatmap(P)