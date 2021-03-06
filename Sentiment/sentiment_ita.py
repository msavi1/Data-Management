# -*- coding: utf-8 -*-
"""sentiment_ita.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkoUkRHSj-lhsBxTy5e3aAUw4S_TIXMb
"""

pip install googletrans

from googletrans import Translator
import pandas as pd

df = pd.read_csv("IT.csv")

df.shape

df.head()

translator = Translator()

df['English_tweet'] = df['text'].apply(translator.translate, src='it', dest='en').apply(getattr, args=('text',))

df.loc[50:60]

#df.to_csv('it_2.csv', index=False)

import pandas as pd
import re

#df = pd.read_csv("it_2.csv")

df.shape

df.head()

df.English_tweet = df.English_tweet.str.lower()

df['text_processed'] = df['English_tweet'].replace("http\S+"," ", regex = True)

df.text_processed = df.text_processed.replace(r'[^\w]'," ", regex = True)

df.text_processed = df.text_processed.replace(r'\d+'," ", regex = True)

df['text_processed'] = df['text_processed'].astype(str).map(lambda x: re.sub(r'\b\w{1}\b', '', x))

df.text_processed = df.text_processed.replace(r'\s+'," ", regex = True)

df.text_processed = df.text_processed.str.lstrip()

df.text_processed = df.text_processed.str.rstrip()

"""Sentiment Analysis"""

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SentimentAnalyzer

sentiment_analyzer = SentimentAnalyzer()

def sentiment_to_label(sentiment_value):
    if( -1 <= sentiment_value <= -0.5):
      return "fortemente negativa"
    elif( -0.5 < sentiment_value < 0):
      return "negativa"
    elif(sentiment_value == 0):
      return "neutra"
    elif( 0 < sentiment_value < 0.5):
      return "positiva"
    elif(sentiment_value >= 0.5):
      return "fortemente positiva"

df_sentiments = df.text_processed.apply(lambda review: sentiment_analyzer.polarity_scores(review))

df['sentiment_score'] = df_sentiments.apply(lambda sentiment: sentiment["compound"])

df.head()

df['sentiment_label'] = df['sentiment_score'].apply(lambda sentiment: sentiment_to_label(sentiment))
df.head()

df[df['sentiment_label'] == 'neutra'].text.iloc[4]

df[df['sentiment_label'] == 'fortemente negativa'].text.iloc[51]

df[df['sentiment_label'] == 'negativa'].text.iloc[21]

df[df['sentiment_label'] == 'positiva'].text.iloc[33]

df[df['sentiment_label'] == 'fortemente positiva'].text.iloc[18]

"""Nairobi"""

df.text = df.text.str.lower()

Nairobi = df[df['text'].str.contains("nairobi")]

Nairobi.shape

len(Nairobi[Nairobi['sentiment_label'] == 'fortemente negativa'])

len(Nairobi[Nairobi['sentiment_label'] == 'negativa'])

len(Nairobi[Nairobi['sentiment_label'] == 'neutra'])

len(Nairobi[Nairobi['sentiment_label'] == 'positiva'])

len(Nairobi[Nairobi['sentiment_label'] == 'fortemente positiva'])

57+30+173+50+69

"""Professore"""

Prof = df[df['text'].str.contains("professore")]

len(Prof)

len(Prof[Prof['sentiment_label'] == 'fortemente negativa'])

len(Prof[Prof['sentiment_label'] == 'negativa'])

len(Prof[Prof['sentiment_label'] == 'neutra'])

len(Prof[Prof['sentiment_label'] == 'positiva'])

len(Prof[Prof['sentiment_label'] == 'fortemente positiva'])

15+12+92+36+18

"""Berlino"""

Berlino = df[df['text'].str.contains("berlino")]
Berlino.shape

len(Berlino[Berlino['sentiment_label'] == 'fortemente negativa'])

len(Berlino[Berlino['sentiment_label'] == 'negativa'])

len(Berlino[Berlino['sentiment_label'] == 'neutra'])

len(Berlino[Berlino['sentiment_label'] == 'positiva'])

len(Berlino[Berlino['sentiment_label'] == 'fortemente positiva'])

31+28+141+56+63

"""Tokyo"""

Tokyo = df[df['text'].str.contains("tokyo|tokio")]

Tokyo.shape

len(Tokyo[Tokyo['sentiment_label'] == 'fortemente negativa'])

len(Tokyo[Tokyo['sentiment_label'] == 'negativa'])

len(Tokyo[Tokyo['sentiment_label'] == 'neutra'])

len(Tokyo[Tokyo['sentiment_label'] == 'positiva'])

len(Tokyo[Tokyo['sentiment_label'] == 'fortemente positiva'])

26+16+109+35+33

"""Rio"""

Rio = df[df['text'].str.contains("río|rio")]

Rio.shape

len(Rio[Rio['sentiment_label'] == 'fortemente negativa'])

len(Rio[Rio['sentiment_label'] == 'negativa'])

len(Rio[Rio['sentiment_label'] == 'neutra'])

len(Rio[Rio['sentiment_label'] == 'positiva'])

len(Rio[Rio['sentiment_label'] == 'fortemente positiva'])

26+22+100+26+29

"""Arturo"""

Arturo = df[df['text'].str.contains("arturo|arturito")]

Arturo.shape

len(Arturo[Arturo['sentiment_label'] == 'fortemente negativa'])

len(Arturo[Arturo['sentiment_label'] == 'negativa'])

len(Arturo[Arturo['sentiment_label'] == 'neutra'])

len(Arturo[Arturo['sentiment_label'] == 'positiva'])

len(Arturo[Arturo['sentiment_label'] == 'fortemente positiva'])

40+29+77+22+6

"""Denver"""

Denver = df[df['text'].str.contains("denver")]

Denver.shape

len(Denver[Denver['sentiment_label'] == 'fortemente negativa'])

len(Denver[Denver['sentiment_label'] == 'negativa'])

len(Denver[Denver['sentiment_label'] == 'neutra'])

len(Denver[Denver['sentiment_label'] == 'positiva'])

len(Denver[Denver['sentiment_label'] == 'fortemente positiva'])

14+10+60+22+20

"""Alicia Sierra"""

A_sierra = df[df['text'].str.contains("alicia sierra|alicia|sierra")]

A_sierra.shape

len(A_sierra[A_sierra['sentiment_label'] == 'fortemente negativa'])

len(A_sierra[A_sierra['sentiment_label'] == 'negativa'])

len(A_sierra[A_sierra['sentiment_label'] == 'neutra'])

len(A_sierra[A_sierra['sentiment_label'] == 'positiva'])

len(A_sierra[A_sierra['sentiment_label'] == 'fortemente positiva'])

13+12+58+21+23

"""Gandia"""

Gandia = df[df['text'].str.contains("césar gandía|cesar gandia|gandia")]
Gandia.shape

len(Gandia[Gandia['sentiment_label'] == 'fortemente negativa'])

len(Gandia[Gandia['sentiment_label'] == 'negativa'])

len(Gandia[Gandia['sentiment_label'] == 'neutra'])

len(Gandia[Gandia['sentiment_label'] == 'positiva'])

len(Gandia[Gandia['sentiment_label'] == 'fortemente positiva'])

16+7+20+8+6

"""Helsinki"""

Helsinki = df[df['text'].str.contains("helsinki")]
Helsinki.shape

len(Helsinki[Helsinki['sentiment_label'] == 'fortemente negativa'])

len(Helsinki[Helsinki['sentiment_label'] == 'negativa'])

len(Helsinki[Helsinki['sentiment_label'] == 'neutra'])

len(Helsinki[Helsinki['sentiment_label'] == 'positiva'])

len(Helsinki[Helsinki['sentiment_label'] == 'fortemente positiva'])

9+7+26+13+10

"""Palermo"""

Palermo = df[df['text'].str.contains("palermo")]
Palermo.shape

len(Palermo[Palermo['sentiment_label'] == 'fortemente negativa'])

len(Palermo[Palermo['sentiment_label'] == 'negativa'])

len(Palermo[Palermo['sentiment_label'] == 'neutra'])

len(Palermo[Palermo['sentiment_label'] == 'positiva'])

len(Palermo[Palermo['sentiment_label'] == 'fortemente positiva'])

24+24+91+34+32

"""Manila"""

Manila = df[df['text'].str.contains("manila")]
Manila.shape

len(Manila[Manila['sentiment_label'] == 'fortemente negativa'])

len(Manila[Manila['sentiment_label'] == 'negativa'])

len(Manila[Manila['sentiment_label'] == 'neutra'])

len(Manila[Manila['sentiment_label'] == 'positiva'])

len(Manila[Manila['sentiment_label'] == 'fortemente positiva'])

1+2+8+4+6

"""Lisbona"""

Lisbona = df[df['text'].str.contains("lisbona")]
Lisbona.shape

len(Lisbona[Lisbona['sentiment_label'] == 'fortemente negativa'])

len(Lisbona[Lisbona['sentiment_label'] == 'negativa'])

len(Lisbona[Lisbona['sentiment_label'] == 'neutra'])

len(Lisbona[Lisbona['sentiment_label'] == 'positiva'])

len(Lisbona[Lisbona['sentiment_label'] == 'fortemente positiva'])

6+2+16+5+11

"""Mosca"""

Mosca = df[df['text'].str.contains("mosca")]
Mosca.shape

len(Mosca[Mosca['sentiment_label'] == 'fortemente negativa'])

len(Mosca[Mosca['sentiment_label'] == 'negativa'])

len(Mosca[Mosca['sentiment_label'] == 'neutra'])

len(Mosca[Mosca['sentiment_label'] == 'positiva'])

len(Mosca[Mosca['sentiment_label'] == 'fortemente positiva'])

7+2+7+3+3

"""Oslo"""

Oslo = df[df['text'].str.contains("oslo")]
Oslo.shape

len(Oslo[Oslo['sentiment_label'] == 'fortemente negativa'])

len(Oslo[Oslo['sentiment_label'] == 'negativa'])

len(Oslo[Oslo['sentiment_label'] == 'neutra'])

len(Oslo[Oslo['sentiment_label'] == 'positiva'])

len(Oslo[Oslo['sentiment_label'] == 'fortemente positiva'])

6+2+6+4+4

"""Bogotà"""

Bogotà = df[df['text'].str.contains("bogotá|bogotà|bogota")]
Bogotà.shape

len(Bogotà[Bogotà['sentiment_label'] == 'fortemente negativa'])

len(Bogotà[Bogotà['sentiment_label'] == 'negativa'])

len(Bogotà[Bogotà['sentiment_label'] == 'neutra'])

len(Bogotà[Bogotà['sentiment_label'] == 'positiva'])

len(Bogotà[Bogotà['sentiment_label'] == 'fortemente positiva'])

4+5+27+4+17

"""Marsiglia"""

Marsiglia = df[df['text'].str.contains("marsiglia")]
Marsiglia.shape

len(Marsiglia[Marsiglia['sentiment_label'] == 'fortemente negativa'])

len(Marsiglia[Marsiglia['sentiment_label'] == 'negativa'])

len(Marsiglia[Marsiglia['sentiment_label'] == 'neutra'])

len(Marsiglia[Marsiglia['sentiment_label'] == 'positiva'])

len(Marsiglia[Marsiglia['sentiment_label'] == 'fortemente positiva'])

2+5+28+16+12

"""Stoccolma"""

Stoccolma = df[df['text'].str.contains("stoccolma")]
Stoccolma.shape

len(Stoccolma[Stoccolma['sentiment_label'] == 'fortemente negativa'])

len(Stoccolma[Stoccolma['sentiment_label'] == 'negativa'])

len(Stoccolma[Stoccolma['sentiment_label'] == 'neutra'])

len(Stoccolma[Stoccolma['sentiment_label'] == 'positiva'])

len(Stoccolma[Stoccolma['sentiment_label'] == 'fortemente positiva'])

4+2+7+7+6

Personaggio = ['Nairobi', 'Professore', 'Berlino', 'Tokyio', 'Rio', 'Arturo', 'Denver', 'Alicia Sierra', 'Gandia', 'Helsinki', 'Palermo', 'Manila',
               'Lisbona', 'Mosca', 'Oslo', 'Bogotà', 'Marsiglia', 'Stoccolma']
Fortemente_negativo = [57, 15, 31, 26, 26, 40, 14, 13, 16, 9, 24, 1, 6, 7, 6, 4, 2, 4]
Negativo = [30, 12, 28, 16, 22, 29, 10, 12, 7, 7, 24, 2, 2, 2, 2, 5, 5, 2]
Neutro = [173, 92, 141, 109, 100, 77, 60, 58, 20, 26, 91, 8, 16, 7, 6, 27, 28, 7]
Positivo = [50, 36, 56, 35, 26, 22, 22, 21, 8, 13, 34, 4, 5, 3, 4, 4, 16, 7]
Fortemente_positivo = [69, 18, 63, 33, 29, 6, 20, 23, 6, 10, 32, 6, 11, 3, 4, 17, 12,6]
N_tweet = [379, 173, 319, 219, 203, 174, 126, 127, 57, 65, 205, 21, 40, 22, 22, 57, 63, 26]

list_of_tuples = list(zip(Personaggio, Fortemente_negativo, Negativo, Neutro, Positivo, Fortemente_positivo, N_tweet))

risultati = pd.DataFrame(list_of_tuples, columns = ['Personaggio', "Fortemente_negativo", "Negativo", "Neutro", "Positivo", "Fortemente_positivo",
                                                    "N_tweet"])
risultati

category_labels = risultati.Personaggio

prova = risultati

totals = [i+j+k+l+m for i,j,k,l,m in zip(prova['Fortemente_negativo'], prova['Negativo'], prova['Neutro'], prova['Positivo'], prova['Fortemente_positivo'])]

F_neg = [i / j * 100 for i,j in zip(prova['Fortemente_negativo'], totals)]

Neg = [i / j * 100 for i,j in zip(prova['Negativo'], totals)]

Neu = [i / j * 100 for i,j in zip(prova['Neutro'], totals)]

Pos = [i / j * 100 for i,j in zip(prova['Positivo'], totals)]

F_pos = [i / j * 100 for i,j in zip(prova['Fortemente_positivo'], totals)]

a = 17

F_neg[a]

Neg[a]

Neu[a]

Pos[a]

F_pos[a]

15+8+27+27+23

import numpy as np
import matplotlib.pyplot as plt


category_names = ['Fortemente negativo', "Negativo", "Neutro", "Positivo", 'Fortemente positivo']
results = {
    'Nairobi': [15, 8, 46, 13, 18],
    'Professore': [9, 7, 53, 21, 10],
    'Berlino':[10, 9, 43, 18, 20], 
    'Tokyio':[12, 7, 50, 16, 15], 
    'Rio': [13, 11, 49, 13, 14],
    'Arturo': [23, 17, 44, 13, 3],
    'Denver': [11, 8, 47, 18, 16], 
    'Alicia Sierra': [10, 9, 46, 17, 18],
    'Gandia': [28, 12, 35, 14, 11], 
    'Helsinki': [14, 11, 40, 20, 15],
    'Palermo': [12, 12, 43, 17, 16], 
    'Manila': [5, 10, 37, 19, 29],
    'Lisbona': [15, 5, 39, 13, 28],
    'Mosca': [32, 9, 31, 14, 14],
    'Oslo': [27, 9, 26, 18, 18],
    'Bogotà': [7, 9, 47, 7, 30],
    'Marsiglia': [3, 8, 44, 26, 19],
    'Stoccolma': [15, 8, 27, 27, 23]
}


def survey(results, category_names):
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 7))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color)
        xcenters = starts + widths / 2

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        for y, (x, c) in enumerate(zip(xcenters, widths)):
            ax.text(x, y, str(int(c)), ha='center', va='center',
                    color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax


survey(results, category_names)
#plt.savefig('Sentiment_personaggi.png')
plt.show()
