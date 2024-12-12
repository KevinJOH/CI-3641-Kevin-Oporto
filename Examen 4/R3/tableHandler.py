class ClassTable:
    def __init__(self):
        self.classes = {}

    def addClass(self, name, methods, superclass=None):
        if name in self.classes:
            print(f"Error: La clase {name} ya existe.")
            return
        
        if superclass and superclass not in self.classes:
            print(f"Error: La clase base {superclass} no existe.")
            return
        
        if len(set(methods)) != len(methods):
            print("Error: Hay definiciones repetidas en la lista de nombres de métodos.")
            return
        
        if self.detectCycle(name, superclass):
            print("Error: Se detectó un ciclo en la jerarquía de herencia.")
            return

        self.classes[name] = {
            "methods": methods,
            "superclass": superclass
        }

    def detectCycle(self, name, superclass):
        visited = set()
        current = superclass
        while current:
            print(current)
            if current in visited:
                return True
            visited.add(current)
            current = self.classes.get(current, {}).get("superclass")
        return False

    def describe(self, name):
        if name not in self.classes:
            print(f"Error: La clase {name} no existe.")
            return
        
        table = self.buildTable(name)
        for method, definition in table.items():
            print(f"{method} -> {definition}")

    def buildTable(self, name):
        table = {}
        currentClass = name
        while currentClass:
            methods = self.classes[currentClass]["methods"]
            for method in methods:
                if method not in table:
                    table[method] = f"{currentClass} :: {method}"
            currentClass = self.classes[currentClass]["superclass"]
        return table

def main():
    Table = ClassTable()
    
    while True:
        command = input("$> ").strip()
        if command.lower() == "salir":
            break
        
        parts = command.split()
        action = parts[0].upper()

        if action == "CLASS":
            name = parts[1]
            if ':' == parts[2]:
                superclass = parts[3]
                name = name.strip()
                superclass = superclass.strip()
                methods = parts[4:]
            else:
                superclass = None
                methods = parts[2:]
            Table.addClass(name, methods, superclass)

        elif action == "DESCRIBIR":
            if len(parts) != 2:
                print("Error: Formato incorrecto para DESCRIBIR.")
                continue
            name = parts[1]
            Table.describe(name)

        else:
            print("Error: Acción no reconocida.")

if __name__ == "__main__":
    main()
