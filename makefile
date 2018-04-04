
cpp_vs_python.png : SebastianSuarez_Graficas.py times_python.csv times_cpp.csv
	python SebastianSuarez_Graficas.py

gen_times.x : 
	c++ gen_times.x

times_python.csv : 
	python SebastianSuarez_GenerarTiempos.py > times_python.csv

times_cpp.csv : SebastianSuarez_GenerarTiempos
	./SebastianSuarez_GenerarTiempos > times_cpp.csv

SebastianSuarez_GenerarTiempos :
	c++ SebastianSuarez_GenerarTiempos.cpp -o SebastianSuarez_GenerarTiempos
