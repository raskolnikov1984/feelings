from process_text import ProcesarTexto
import time

if __name__ == "__main__":
    print("Iniciando análisis...\n")
    time.sleep(3)

    # Ruta a los archivos crudos.
    ruta_datos = 'data/'

    # Archivo CSV para leer nube de palabras
    nube_palabras = ruta_datos + 'nube_palabras_base.csv'

    # Propuesta Medellín creemos en vos
    # Lectura del archivo en texto plano.
    medellin_creemos_en_vos = 'data/medellin_creemos_en_vos.txt'

    # Se instancia obejto para procesar texto
    primera_propuesta = ProcesarTexto(
        medellin_creemos_en_vos, nube_palabras)
    programa_grobierno_primera_propuesta = \
        primera_propuesta.leer_archivo_texto()
    # print(type(programa_grobierno_primera_propuesta))
    print(primera_propuesta.tokenizar_texto(programa_grobierno_primera_propuesta, 'oraciones')[2])
    # nube_palabras = primera_propuesta.leer_nube_palabras()
    # nube_estructurada = primera_propuesta.estructurar_nube_palabras(
    #     nube_palabras)

    # time.sleep(3)
    # print(nube_estructurada)

    # print(nube_estructurada.values())
    # for tema, valor in nube_estructurada.items():
    #     print(tema+'\n')
    #     print(str(valor)+'\n')
    #     time.sleep(2)
