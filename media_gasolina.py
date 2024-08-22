# código de geração do gráfico 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')
sns.lineplot(data=df, x='dia', y='venda')

plt.title('Preço Médio da Gasolina em São Paulo - 10 Primeiros Dias de Julho 2021')
plt.xlabel('Dia')
plt.ylabel('Preço')

plt.savefig('gasolina.png')