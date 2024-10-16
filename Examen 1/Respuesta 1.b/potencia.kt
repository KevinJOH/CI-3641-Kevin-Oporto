/*
	Kevin Oporto ; 13-11007
	Lenguajes de Programación I
	Examen I
	Pregunta 1.b.i) Dados 3 enteros a, b y c calcula (a^b) mod c
*/
import kotlin.math.pow

/*
	Simplemente toma 3 numeros enteros a, b y c y calcula (a^b) mod c
	Verificar si b = 0, se retorna 1 automaticamente
	Si no, retornar (a^b)%c
*/

fun modPow(a:Int, b:Int, c: Int):Int{
	
    if (b == 0){	
        return 1
    } else {
        return ((a.toDouble().pow(b)).toInt())%c
    }
}
/*
	Funcion principal, que recibe 3 enteros y llama a modPow.
*/
fun main() {
	val a = 5
	val b = 2
	val c = 3
    val res = modPow(a, b, c)
	println("Tenemos que el resultado de (${a} ^ ${b}) mod ${c} es: ")
    println(res)
}