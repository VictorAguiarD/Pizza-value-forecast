import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Carrega o dataset
df = pd.read_csv("pizzas.csv")

# Cria e treina o modelo de regressão linear
modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]
modelo.fit(x, y)

# Título do app
st.title("Prevendo o valor de uma pizza")
st.divider()

# Input para o usuário inserir o diâmetro
diametro = st.number_input("Digite o tamanho do diâmetro da pizza:")

# Definindo limites de aceitação do diâmetro
diametro_min = 10
diametro_max = 49.99

# Verifica se o usuário inseriu um diâmetro
if diametro:
    # Verifica se o diâmetro está dentro dos limites aceitos
    if diametro_min <= diametro <= diametro_max:
        preco_previsto = modelo.predict([[diametro]])[0][0]
        st.write(f"O valor da pizza com diâmetro de {diametro:.2f} cm é de R${preco_previsto:.2f}")
        st.success(f"Pizza de diâmetro de {diametro:.2f} cm foi aceita com sucesso", icon="✅")
        st.balloons()
    #Caso o diâmetro esteja menor que o permitido
    elif diametro < diametro_min:
       st.error(f"Pizza de diâmetro {diametro:.2f} cm não foi aceito , peça um diâmetro maior que 9,99 cm", icon="🚫");

    else:
        # Caso o diâmetro esteja fora do intervalo aceito
        st.error(f"Pizza de diâmetro {diametro:.2f} cm não foi aceito , peça um diâmetro menor que 50 cm", icon="🚫")
    