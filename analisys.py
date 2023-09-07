# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
import nltk

try:
    nltk.data.find('tokenizers/punkt')
    print("El modelo 'punkt' de NLTK está disponible en el sistema.")
except LookupError:
    print("El modelo 'punkt' de NLTK no está disponible en tu sistema. \
    Debes descargarlo.")

if not nltk.data.find('tokenizers/punkt'):
    print("Instalando punkt...\n")
    nltk.download('punkt')


class ProcessText:
    "Class for the processing analisys of cloud word"
    __name__ = 'feelings.process_cloud_word'

    def __init__(self, text,):
        pass


if __name__ == "__main__":
    print("Iniciando análisis...")
