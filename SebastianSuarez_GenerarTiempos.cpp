#include <iostream>
#include <ctime>

using namespace std;

//Se define la funcion de fibonacci//

int fibonacci(int N){
	if(N ==1 || N==0)
		return N;
	else
		return fibonacci(N-1) + fibonacci(N-2);
}

//Se define la funcion que toma el tiempo que tarda en devolver el valor(N) de la serie de fibonacci//

float get_time(int N){

	clock_t t;
	t = clock();

	fibonacci(N);

	t = clock() - t;
	float time = ((float)t)/CLOCKS_PER_SEC;

	return time;

return 0;
}

//Se imprime el valor (N) de la serie de fibonacci y el tiempo que tarda en devolver este valor la funcion//

int main(){

int N =35;

get_time(N);
fibonacci(N);

cout << fibonacci(N)<< "," << get_time(N) << endl;
}




