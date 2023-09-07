# Provee información del sistema
from os import path
# TODO: Reemplazar PIL por PILLOW
# (Python Imaging Library)
from PIL import image
# Generación de nubes de palabras
from wordcloud import Wordcloud, STOPWORDS, ImageColorGenerator
# Computación cientifica, Manejo de
# Arreglos y matrices
import numpy as np
# Manipulación y analisis de datos
import pandas as pd
# funciones para crear y personalizar gráficos y
# visualizaciones.
import matplotlib.pyplot as plt
# %matplotlib inline

# Load in the dataframe
df = pd.read_csv("data/winemag-data-130k-v2.csv", index_col=0)
# Looking at first 5 rows of the dataset
df.head()

print("There are {} observations and {} features in this dataset. \n".format(df.shape[0],df.shape[1]))
print("There are {} types of wine in this dataset such as {}... \n".format(len(df.variety.unique()),
                                                                           ", ".join(df.variety.unique()[0:5])))
print("There are {} countries producing wine in this dataset such as {}... \n".format(len(df.country.unique()),
                                                                                      ", ".join(df.country.unique()[0:5]))

# This code uses pandas library in Python to select and display
# the first five rows of a DataFrame (df) with only the columns
# "country", "description", and "points".
df[["country", "description","points"]].head()

# Groupby by country
country = df.groupby("country")

# Summary statistic of all countries
country.describe().head()

country.mean().sort_values(by="points",ascending=False).head()

plt.figure(figsize=(15,10))
country.size().sort_values(ascending=False).plot.bar()
plt.xticks(rotation=50)
plt.xlabel("Country of Origin")
plt.ylabel("Number of Wines")
plt.show()

# plt.figure(figsize=(15,10))
# country.max().sort_values(by="points",ascending=False)["points"].plot.bar()
# plt.xticks(rotation=50)
# plt.xlabel("Country of Origin")
# plt.ylabel("Highest point of Wines")
# plt.show()
