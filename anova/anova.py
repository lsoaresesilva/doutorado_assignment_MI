import pandas as pd
import statsmodels.api as sm
from statsmodels.graphics.factorplots import interaction_plot
from scipy import stats
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

dados = pd.read_csv("completeout.csv")

dados_quick = dados[dados.algoritmo == "bubble"]
#print(dados_quick.columns)
print(dados_quick.index.nlevels)
#fig = interaction_plot(dados_quick.tamanho_array, dados_quick.probabilidade, dados.tamanho_sub_array_ordenado, colors=['red','blue', "green", "yellow"], ms=10)
#plt.show()

formula = 'tamanho_sub_array_ordenado ~ C(tamanho_array) + C(probabilidade) + C(tamanho_array):C(probabilidade)'
model = ols(formula, dados_quick).fit()
aov_table = anova_lm(model, typ=2)
print(aov_table)
res = model.resid 
#fig = sm.qqplot(res, line='s')
print("Shapiro-wilk test")
print(stats.shapiro(res))
plt.show()

