# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
import nltk
import csv

try:
    nltk.data.find('tokenizers/punkt')
    print("El modelo 'punkt' de NLTK está disponible en el sistema.")
except LookupError:
    print("El modelo 'punkt' de NLTK no está disponible en tu sistema. \
    Debes descargarlo.")

if not nltk.data.find('tokenizers/punkt'):
    print("Instalando punkt...\n")
    nltk.download('punkt')


class ProcesarTexto:
    "Class for the processing analisys of cloud word"
    __name__ = 'feelings.process_cloud_word'

    def __init__(self, text):
        pass

    def leer_nube_palabras(self, nombre_archivo):
        """
        Recibe  un archivo csv, el cual consta de 3
        columnas:

        ...Tema:
        ...Propuesta principal:
        ...Propuesta específica:
        ...Secuencia de palabras:
        ...Puntos:

        Retorna una lista de lista con cada fila leída del archivo csv.
        """
        datos = []
        with open(nombre_archivo, mode='r', newline='') as archivo:
            lector_csv = csv.reader(archivo, delimiter=':')
            for fila in lector_csv:
                datos.append(fila)
        return datos

    def estructurar_nube_palabras(self, datos):
        """
        Recibe una lista de listas de string que obtine de la función
        leer_nube_palabras.

        Retorna un diccionario de la forma:
        {'Tema': {'Propuesta principal': {'Propuesta específica':
        'Secuencia de palabras'}}}
        """
        propuesta_consolidada = {}
        for dato in datos:
            tema = dato[0]
            propuesta_principal = dato[1]
            propuesta_especifica = dato[2]
            secuencia_palabras = dato[3]
            temas = propuesta_consolidada.keys()
            if dato[0] not in temas:
                propuesta_consolidada[tema] = {
                    propuesta_principal: {
                        propuesta_especifica:
                        secuencia_palabras}}
            else:
                if propuesta_principal not in propuesta_consolidada[tema]:
                    propuesta_consolidada[tema][propuesta_principal] = {
                            propuesta_especifica:
                            secuencia_palabras}
                else:
                    propuesta_consolidada[tema][propuesta_principal][propuesta_especifica] = \
                        secuencia_palabras

        return propuesta_consolidada


if __name__ == "__main__":
    print("Iniciando análisis...")
