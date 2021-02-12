
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

teta = np.linspace(-np.pi/2,np.pi/2,500)
sin_teta = np.sin(teta)
(a,b) = np.meshgrid(sin_teta,sin_teta)

#Parámetros de la abertura para un caso particular en metros

#Sí se toman valores entre 0.00009 a 0.000001 para la abertura se verá el patron, 
#entre mas pequeña la abertura mejor se vera el patron de difracción
ancho = 0.000005      
alto =  0.000005
x_0 = ancho/2
y_0 = alto/2
R = 10                                             #distancia entre la abertura y la pantalla
A = ancho*alto                                     #área de la abertura

#Parámetros de la onda electromagnética en el vacío en el SI
lamda = 7*10**(-7)                                 #longitud de onda de la luz roja
k = 2*np.pi/lamda                                  #número de onda
epsilon_0 = 8.8541878176*10**(-12)                 #permitividad electrica
mu_0 = 4*np.pi*10**(-7)                            #permeabilidad magnética

#Campo difractado e Irradiancia
alfa = x_0*k
beta = y_0*k
I_0 =(1/2)*np.sqrt(epsilon_0/mu_0)*(1/2)*(A/R)**2  #irradiancia original 

def z(x, y):
    sinc_x = (np.sin(alfa*x)/(alfa*x))
    sinc_y = (np.sin(beta*y)/(beta*y))
    return I_0*(sinc_x**2)*(sinc_y**2)

fig = plt.figure()
ax = Axes3D(fig)
ax.contourf(a,b,z(a,b),vmin=0, vmax=I_0/20,levels=1000,cmap='hot')
plt.xlabel('Eje Z')
plt.ylabel('Eje Y')
plt.show()
