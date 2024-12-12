class Grafo
	def initialize
		@list = {}
	end

    def agregarArco(origen, destino)
        @list[origen] ||= []
        @list[origen] << destino
    @list[destino] ||= []
    end

    def vecinos(nodo)
        @list[nodo]
    end

    def nodos
        @list.keys
    end
end

class Busqueda
    def initialize(grafo)
        @grafo = grafo
    end

    def buscar(d, h)
        visitados = {}
        pila = [d]
        nodosExplorados = 0

        while !pila.empty?
            nodo = pila.pop
            next if visitados[nodo]
        
            visitados[nodo] = true
            nodosExplorados += 1
            return nodosExplorados if nodo == h

            vecinos = @grafo.vecinos(nodo)
            vecinos.each { |vecino| pila.push(vecino) unless visitados[vecino] }
        end
        -1
    end
end

class DFS < Busqueda
end

class BFS < Busqueda
    def buscar(d, h)
        visitados = {}
        cola = [d]
        nodosExplorados = 0

        while !cola.empty?
            nodo = cola.shift
            next if visitados[nodo]

            visitados[nodo] = true
            nodosExplorados += 1
            return nodosExplorados if nodo == h

            vecinos = @grafo.vecinos(nodo)
            vecinos.each { |vecino| cola.push(vecino) unless visitados[vecino] }
        end
        -1
    end
end