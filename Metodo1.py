# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 14:53:30 2022

@author: josem
"""

import numpy as np
import re
from numpy.random import seed
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

"""Combine la matriz de nodos con el vector que contiene los valores de la temperatura """
# l=  np.insert(arrayNodos,arrayNodos.shape[1],arrayTemperature,1)
"""Abro el TXT para escribir  la matrix """
# with open('test.txt', 'w') as fout:
"""Escritura de matrix con caracteres para luego separar (#)"""    
#     fout.write(u'#'+'\t'.join(str(e) for e in l.shape)+'\n')
"""Escribe una matriz en un archivo como texto o binario"""
#     l.tofile(fout)


"""Se pasa de texto a """

with open('test.txt', 'rb') as f:
    line=f.readline().decode('ascii')
    if line.startswith('#'):
        shape=tuple(map(int, re.findall(r'(\d+)', line)))
    else:
        raise IOError('Fallo al encontrar la matrix')    

    result2=np.fromfile(f)
    result3=result2.reshape(shape)

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
        