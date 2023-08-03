import pandas as pd
import plotly.express as px

# Passo1: Importar a base de dados
# axis = 0 se for linha
# axis = 1 se for coluna

# Passo2: Visualizar a base de dados
tabela = pd.read_csv("analise de dados/clientes.csv", encoding="latin", sep=";")
# print(tabela)

# Passo3: Tratamento de Dados
tabela = tabela.drop("Unnamed: 8", axis=1)
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")
tabela = tabela.dropna()
# print(tabela.info())
# print(tabela.describe())


# Passo4: Analise inicial
# grafico = px.histogram(tabela,x="Profissão",y="Nota (1-100)", histfunc="avg", text_auto=True)

# grafico.show()


# Passo5: Analise completa
for coluna in tabela.columns:
    grafico = px.histogram(tabela,x=coluna,y="Nota (1-100)", histfunc="avg", text_auto=True)
    grafico.show()
