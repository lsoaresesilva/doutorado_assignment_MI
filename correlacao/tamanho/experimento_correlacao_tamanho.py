import pandas as pd
import numpy as np
#from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

documento = pd.read_csv("dados_tamanho.csv")
#print(pd.to_numeric(documento["tamanho_array"]))
#documento['tamanho_array'].astype(object).astype(str)
print(documento.dtypes)
quick_data_10 = documento[(documento.algoritmo=="insertion") & (documento.tamanho_array==10)]

media_10_t_sub_array = quick_data_10["tamanho_sub_array_ordenado"].mean()

quick_data_50 = documento[(documento.algoritmo=="insertion") & (documento.tamanho_array==50)]
media_50_t_sub_array = quick_data_50["tamanho_sub_array_ordenado"].mean()

quick_data_100 = documento[(documento.algoritmo=="insertion") & (documento.tamanho_array==100)]
media_100_t_sub_array = quick_data_100["tamanho_sub_array_ordenado"].mean()

quick_data_1000 = documento[(documento.algoritmo=="insertion") & (documento.tamanho_array==1000)]
media_1000_t_sub_array = quick_data_1000["tamanho_sub_array_ordenado"].mean()

quick_data_10000 = documento[(documento.algoritmo=="insertion") & (documento.tamanho_array==10000)]
media_10000_t_sub_array = quick_data_10000["tamanho_sub_array_ordenado"].mean()



plt.scatter(np.array([10, 50, 100, 1000, 10000]), np.array([media_10_t_sub_array, media_50_t_sub_array, media_100_t_sub_array, media_1000_t_sub_array, media_10000_t_sub_array]))
plt.show()

#model = ols('tamanho_sub_array_ordenado ~ C(algoritmo)*C(tamanho_array)', algo_probabilidade_01).fit()
#print(model.)