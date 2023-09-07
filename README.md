# feelings
This is a repository for the sentimental analysis for government proposals for Medellin city.

### Limpiar el Espacio de Trabajo y Cargar Bibliotecas:
   * Elimina todos los objetos del espacio de trabajo actual y carga las bibliotecas necesarias.
   
### Palabras de Detención Personalizadas:
   * Crea palabras de detención personalizadas en español combinando las palabras de detención incorporadas
   con palabras adicionales de la lista de palabras de detención de la libreria NLTK.

### Leer Datos CSV:
   * Lee los datos de un archivo de Excel llamado "nube_palabras_base.csv"..

### Tokenización:
   * Divide en tokens el texto de la columna "Secuencia de Palabras" del marco de datos leido anteriormente
   y elimina las palabras de detención personalizadas.

### Análisis de Frecuencia de Palabras:
   * Realiza un análisis de frecuencia de palabras y crea un gráfico de barras de las palabras más frecuentes
     (palabras que ocurren más de una cantidad de veces, ejemplo 50) en el texto.
     
### Nube de Palabras:
   * Genera una nube de palabras a partir de los datos de texto.

### Tokenización de programa de gobierno:
   * Divide en tokens todo el conjunto de datos y almacena los tokens en texto_palabras.
   
### Análisis de Sentimientos - Parte 1:
   * Realiza un análisis de sentimientos en el texto tokenizado 'medellin_creemos_en_vos.txt'.

### Análisis de Sentimientos - Parte 2:
   * Realiza un análisis de sentimientos en todo el conjunto de datos y almacena los resultados  con base en la nube de palabras personalizadas.

### Gráfico de Barras de Emociones:
   * Crea un gráfico de barras de las emociones basado en los resultados del análisis de sentimientos.

### En general para los analisis de sentimientos:
   ### TODO: Reemplazar con conceptos afín del interes en el análisis de propuestas
   * Palabras Asociadas con Tristeza:
     Identifica	y lista las palabras asociadas con la tristeza basadas en el análisis de sentimientos.

   * Palabras Asociadas con Confianza:
     Identifica y lista las palabras asociadas con la confianza basadas en el análisis de sentimientos.
   
   * Nube de Palabras de Emociones:
     Genera una nube de palabras para diferentes emociones (tristeza, alegría, enojo, miedo) utilizando los datos de texto tokenizados.

   *  Matriz Término-Documento (TDM):
      Crea una Matriz Término-Documento a partir de los datos de texto tokenizados,
      representando las frecuencias de palabras en diferentes emociones (tristeza, alegría, enojo, confianza).
   *  Nube de Palabras de Emociones: Genera una nube de palabras de comparación
      para visualizar las frecuencias de palabras asociadas con diferentes emociones.