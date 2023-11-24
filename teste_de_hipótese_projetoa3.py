# -*- coding: utf-8 -*-
"""Teste de Hipótese - ProjetoA3.ipynb

import pandas as pd
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
print(df)

import numpy as np
import scipy.stats

qualidadeDeSono_PessoasQueFazemExercicio = df[df['Physical Activity Level']>= 60]["Quality of Sleep"]
qualidadeDeSono_PessoasQueNaoFazemExercicio = df[df['Physical Activity Level']<60]["Quality of Sleep"]

nx = len(qualidadeDeSono_PessoasQueFazemExercicio)
ny = len(qualidadeDeSono_PessoasQueNaoFazemExercicio)

mediaX = np.average(qualidadeDeSono_PessoasQueFazemExercicio)
mediaY = np.average(qualidadeDeSono_PessoasQueNaoFazemExercicio)

desvioX = np.std(qualidadeDeSono_PessoasQueFazemExercicio)
desvioY = np.std(qualidadeDeSono_PessoasQueNaoFazemExercicio)

T = (mediaX - mediaY)/np.sqrt((desvioX**2/nx)+(desvioY**2/ny))
print(T)


print(scipy.stats.t.isf(0.025, 372))

"""Hipótese alternativa confirmada, já que nosso Test T tem um valor maior que o valor da Região Crítica."""
