class Secuencia
    def agregar(elemento)
        @elementos.push(elemento)
    end

    def remover
        raise 'La pila está vacía' if vacio
        @elementos.pop
    end

    def vacio
        @elementos.empty?
    end
end

class Pila < Secuencia
    def initialize
        @elementos = []
    end
end

class Cola < Secuencia
    def initialize
        @elementos = []
    end
    def remover
        raise 'La cola está vacía' if vacio
        @elementos.shift
    end
end
