Algoritmo reto2
	
    Definir n, suma, i, dado Como Entero;
	
    suma <- 0;
	
    Escribir "Por favor, ingresa el número de veces que quieres lanzar el dado:";
    Leer n;
	
    Para i <- 1 Hasta n Con Paso 1 Hacer

        dado <- azar(6) + 1;
		
        suma <- suma + dado;
    FinPara
	
    Escribir "##### Resultado Final #####";
    Escribir "Después de ", n, " lanzamientos, la suma total de los dados es: ", suma;

FinAlgoritmo