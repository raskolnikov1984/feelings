from nltk.tokenize import sent_tokenize, word_tokenize
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

    def leer_archivo_texto(ruta_archivo):
        """
        Lee un archivo de texto plano y devuelve su contenido.
        ..ruta_archivo (str): La ruta del archivo de texto a leer.
        Retorna str: El contenido del archivo de texto.

        # Ejemplo de uso
        ruta_del_archivo = "mi_archivo.txt"
        contenido_del_archivo = leer_archivo_texto(ruta_del_archivo)
        print(contenido_del_archivo)
        """
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
            return contenido
        except FileNotFoundError:
            return "El archivo no fue encontrado."
        except Exception as e:
            return f"Error al leer el archivo: {str(e)}"

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

    def tokenizar_texto(texto, tipo='palabras', idioma='spanish'):
        """
        Tokeniza un texto en oraciones o palabras.
        Recibe:
        texto (str): El texto que se va a tokenizar.
        tipo (str): El tipo de tokenización ('oraciones' o 'palabras').
        Por defecto, es 'palabras'.
        idioma (str): El idioma en el que se encuentra el texto.
        Por defecto, es 'spanish'.

        Returns:
        list: Una lista de oraciones o palabras tokenizadas.
        """
        if tipo == 'palabras':
            return word_tokenize(texto, language=idioma)
        elif tipo == 'oraciones':
            return sent_tokenize(texto, language=idioma)
        else:
            raise ValueError(
                "El tipo de tokenización debe ser 'palabras' o 'oraciones'.")


if __name__ == "__main__":
    print("Iniciando análisis...")
