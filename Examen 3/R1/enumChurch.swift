// 1.b.i)
import Foundation

indirect enum Church {
	case cero
	case suc(Church)
}

func suma(_ a: Church, _ b: Church) -> Church {
	switch a {
	case .cero:
		return b
	case let .suc(n):
		return .suc(suma(n, b))
	}
}

func multiplicacion(_ a: Church, _ b: Church) -> Church {
	switch a {
	case .cero:
		return .cero
	case let .suc(n):
		return suma(b, multiplicacion(n, b))
	}
}

let cero = Church.cero
let uno = Church.suc(cero)
let dos = Church.suc(uno)
let tres = Church.suc(dos)

func churchToInt(_ c: Church) -> Int {
	switch c {
	case .cero:
		return 0
	case let .suc(n):
		return 1 + churchToInt(n)
	}
}

let sumaResultado = suma(uno, dos)
print("Suma de 1 y 2: \(churchToInt(sumaResultado))")

let multiplicacionResultado = multiplicacion(dos, tres)
print("Multiplicación de 2 y 3: \(churchToInt(multiplicacionResultado))")
