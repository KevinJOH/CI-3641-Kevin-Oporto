// 1.b.ii)
import Foundation

struct Persona {
	var nombre: String
	var edad: Int
}

struct ConjuntoDePersonas {
	var personas: [Persona]
    
	func cantidadDePersonas() -> Int {
		return personas.count
	}
    
	func mayoresDeEdad() -> [Persona] {
		return personas.filter { $0.edad >= 18 }
	}
    
	func nombreMasComun() -> String? {
		let nombres = personas.map { $0.nombre }
		let nombreFrecuencias = nombres.reduce(into: [:]) { counts, nombre in
			counts[nombre, default: 0] += 1
		}
		return nombreFrecuencias.max(by: { $0.value < $1.value })?.key
	}
}

// Ejemplo para probar las funciones:

let personas: [Persona] = [
	Persona(nombre: "Ana", edad: 20),
	Persona(nombre: "Alvaro", edad: 15),
	Persona(nombre: "Ana", edad: 17),
	Persona(nombre: "Pedro", edad: 18),
	Persona(nombre: "Luis", edad: 30)
]

let conjunto = ConjuntoDePersonas(personas: personas)

print("Cantidad de personas en el conjunto: \(conjunto.cantidadDePersonas())")

let mayores = conjunto.mayoresDeEdad()
print("Los mayores de edad del conjunto son:")
for persona in mayores {
	print("Nombre: \(persona.nombre), Edad: \(persona.edad)")
}

if let nombreComun = conjunto.nombreMasComun() {
	print("Nombre más común en el conjunto: \(nombreComun)")
} else {
	print("No hay nombres en el conjunto.")
}
