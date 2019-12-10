import pandas as pd
import numpy as np
#from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

documento = pd.read_csv("dados_probabilidade.csv")

quick_data_0_1 = documento[(documento.algoritmo=="quick") & (documento.probabilidade==0.1)]
media_0_1_t_sub_array = quick_data_0_1["tamanho_sub_array_ordenado"].mean()

quick_data_0_15 = documento[(documento.algoritmo=="quick") & (documento.probabilidade==0.15)]
media_0_15_t_sub_array = quick_data_0_15["tamanho_sub_array_ordenado"].mean()

quick_data_0_25 = documento[(documento.algoritmo=="quick") & (documento.probabilidade==0.25)]
media_0_25_t_sub_array = quick_data_0_25["tamanho_sub_array_ordenado"].mean()

quick_data_0_5 = documento[(documento.algoritmo=="quick") & (documento.probabilidade==0.5)]
media_0_5_t_sub_array = quick_data_0_5["tamanho_sub_array_ordenado"].mean()

quick_data_0_6 = documento[(documento.algoritmo=="quick") & (documento.probabilidade==0.6)]
media_0_6_t_sub_array = quick_data_0_6["tamanho_sub_array_ordenado"].mean()

quick_data_0_75 = documento[(documento.algoritmo=="quick") & (documento.probabilidade==0.75)]
media_0_75_t_sub_array = quick_data_0_75["tamanho_sub_array_ordenado"].mean()

quick_data_0_9 = documento[(documento.algoritmo=="quick") & (documento.probabilidade==0.9)]
media_0_9_t_sub_array = quick_data_0_9["tamanho_sub_array_ordenado"].mean()

plt.scatter(np.array([0.1, 0.15, 0.25, 0.5, 0.6, 0.75, 0.9]), np.array([media_0_1_t_sub_array, media_0_15_t_sub_array, media_0_25_t_sub_array, media_0_5_t_sub_array, media_0_6_t_sub_array, media_0_75_t_sub_array, media_0_9_t_sub_array]))
plt.show()
#model = ols('tamanho_sub_array_ordenado ~ C(algoritmo)*C(tamanho_array)', algo_probabilidade_01).fit()
#print(model.)