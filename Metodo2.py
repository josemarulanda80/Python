# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 16:31:00 2022

@author: josem
"""
import numpy as np

import numpy as np
import re
from numpy.random import seed
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

"""Se crea una matrix que es la combinación de la matrix nodos mas el arreglo con los valores de la tremperatura """
      # l=  np.insert(arrayNodos,arrayNodos.shape[1],arrayTemperature,1)
      #    np.savetxt("test2.txt", l)
result3= np.loadtxt("test2.txt")


def postProceso(x1,y1,z1,text):
        seed(1234)
        x = x1
        y =y1
        z =z1
        # define grid.
        xi = np.linspace(0,1,1000)
        yi = np.linspace(0,1,1000)
        # grid the data.
        zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')
        plt.contourf(xi,yi,zi,50,vmin=0,vmax=100,cmap=plt.cm.jet)
        m = plt.cm.ScalarMappable(cmap=plt.cm.jet)
        m.set_array(zi)
        m.set_clim(0., 100)
        plt.colorbar(m, boundaries=np.linspace(0, 100, 10))
        plt.xlim(0,1)
        plt.ylim(0,1)
        plt.title(text)
        
postProceso(result3[:,0],result3[:,1],result3[:,4],'Mapa calor de prueba ')        
        