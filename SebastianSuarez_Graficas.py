import numpy as np
import matplotlib.pyplot as plt

#Carga los archivos times_python.csv y times_cpp

dataTPy = np.loadtxt('times_python.csv')
dataTCp = np.loadtxt('times_python.csv')

NxPy = dataTPy[:,0]
timePy = dataTPy[:,1]

NxCP = dataTCp[:,0]
timeCp = dataTCp[:,1]

#Grafica los tiempos y N de python y los de c++ en una misma grafica

plt.figure()

plt.plot(NxPy, timePy, color = 'k')
plt.plot(NxCP, timeCp, color = 'r')

plt.xlabel("N")
plt.ylabel("Time (anos)")
plt.title("Tiempo vs N")

plt.savefig("cpp_vs_python.png")
