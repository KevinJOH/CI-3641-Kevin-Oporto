% Respuesta 1.b.i
% Dada una funcion f(n), donde n/2, si n es par y 3n+1 si n es impar
% Devuelve el número de repeticiones consecutivas a f(n) hasta llegar a 1

% Funcion dada
function result = f(n)
	if mod(n, 2) == 0
		result = n / 2;
	else
		result = 3 * n + 1;
	end
end

% Contador de repeticion de la funcion
function c = count(n)
	c = 0;
	while n != 1
		n = f(n);
		c++;
	end
end

% Asignamos el valor a n y llamamos a count imprimiendolo
n = 42;
disp(count(n));  
