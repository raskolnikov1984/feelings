from nltk.tokenize import sent_tokenize, word_tokenize
# Palabras Vacías
from nltk.corpus import stopwords
# Raíz de una palabra
from nltk.stem import PorterStemmer
# Obtener el lema de una palabra
from nltk.stem import WordNetLemmatizer
import nltk
import csv

__all__ = ['ProcessLookupError']

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    print("El modelo 'punkt' de NLTK no está disponible en tu sistema. \
    Debes descargarlo.")

if not nltk.data.find('tokenizers/punkt'):
    print("Instalando punkt...\n")
    nltk.download('punkt')


class ProcesarTexto:
    "Class for the processing analisys of cloud word"
    __name__ = 'feelings.process_cloud_word'

    def __init__(self, ruta_propuesta, nube_palabras):
        self.ruta_propuesta = ruta_propuesta
        self.nube_palabras = nube_palabras

    def leer_archivo_texto(self):
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
            with open(self.ruta_propuesta, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
            return contenido
        except FileNotFoundError:
            return "El archivo no fue encontrado."
        except Exception as e:
            return f"Error al leer el archivo: {str(e)}"

    def leer_nube_palabras(self):
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
        with open(self.nube_palabras, mode='r', newline='') as archivo:
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

    def tokenizar_texto(self, texto, tipo='palabras', idioma='spanish'):
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

    def procesar_unidad_sentido():
        """
        Recibe una unidad de Sentido (Oración, texto con sentido).
        Limpia las palabras vacías (palbras que no aportan sentido).
        Recibe:
        texto (str): El texto que va a limpiar.
        Retorna una lista procesada con las palabras de la unidad de sentido
        """

        """
        TODO: Verificar necidad de identificar partes del habla
        Sustanvito, Pronombre, Adjetivo, Verbo...
        """
        oracion = ""
        destilador = PorterStemmer()
        # lematizador = WordNetLemmatizer()
        palabras_vacias = set(stopwords.words("spanish"))
        palabras_oracion = word_tokenize(oracion)

        oracion_filtrada = [destilador.stem(palabra.lower())
                            for palabra in palabras_oracion if
                            palabra.casefold() not in palabras_vacias]

        # oracion_lematizada = [lematizador.lemmatize(palabra.lower())
        #                       for palabra in palabras_oracion if
        #                       palabra.casefold() not in palabras_vacias]

        if not oracion_filtrada:
            return
        return oracion_filtrada

    def match_palabras(nube_palabras: set, programa_grobierno: set) -> set:
        return nube_palabras.intersection(programa_grobierno)

    def son_disjuntos(nube_palabras: set, programa_grobierno: set) -> bool:
        return nube_palabras.isdisjoint(programa_grobierno)


"""
TODO: Realizar busquedas de palabras utilizando teoria de conjuntos.

palabras_destiladas = [
'gran', 'alianza', 'primera',
'infancia', 'medellín', 'haremo',
'travé', 'diversa', 'secretaría',
'departamento', 'administrativo',
'alcaldía', 'medellín', ',',
'junto', 'sector', 'académico',
',', 'empresarial', ',',
'civil', ',', 'comunitario',
',', ',', 'consolidar', 'distrito',
'ciudad', 'promuev', 'desarrollo',
'infantil', 'manera', 'integr', '.'
]
In [55]: {'empresarial','gran','ciudad'}.intersection(palabras_destiladas)
Out[55]: {'ciudad', 'empresarial', 'gran'}


busquedas de unidades de sentido compuestas

In [54]: 'empresarial' and 'gran' and 'ciudad' in stemmed_words
Out[54]: True
"""

"""
Hacer una trama de dispersión
Puedes usar un parcela de dispersión para ver cuánto aparece una palabra en
particular y dónde aparece. Hasta ahora, hemos buscado "man" y "woman",
pero sería interesante ver cuánto se usan esas palabras
en comparación con sus sinónimos:

text8.dispersion_plot(
...     ["woman", "lady", "girl", "gal", "man", "gentleman", "boy", "guy"]
... )
"""

"""
import spacy

nlp = spacy.load('es_core_news_sm')
texto = "Texto"
doc = nlp(texto)

for oracion in doc.sents:
print(oracion.text)
"""
