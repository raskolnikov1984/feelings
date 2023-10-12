import matplotlib.pyplot as plt

class Reporte():
    "class for the realization the graphics or reports for the project"
    __name__ = 'feelings.reports'

    def __init__(self, data):
        self.data = data

    def get_axisx_axisy(self):
        return [
            list(self.data.keys()),
            list(self.data.values())
        ]

    def mostrar_diagrama_de_barras(self):
        palabras, frecuencias = self.get_axisx_axisy()
        if len(palabras) != len(frecuencias):
            raise ValueError("Las listas de palabras y frecuencias deben tener la misma longitud.")
        
        plt.figure(figsize=(10, 6)) 
        plt.barh(palabras, frecuencias, color='skyblue') 
        plt.xlabel('Frecuencia')
        plt.ylabel('Palabra')
        plt.title('Diagrama de Barras Horizontal de Frecuencias')
        #plt.gca().invert_yaxis()
        plt.show()
