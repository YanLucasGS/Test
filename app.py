import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='App AEDA',page_icon="bar_chart:")
def main():
    # st.markdown("""
    # # Olá 2DTSR, esta é o nosso primeiro app em streamlit!

    # ## Este é meu subtítulo no app!

    # ### Estou diminuindo mais ainda

    # - primeiro item
    # - sgundo item
    # - terceiro item

    # """)

    # lista_user = ["matheus.pavani", "eder.santos"]

    # x = st.text_input("Digite seu usuário")

    # if x in lista_user:
    #     st.success("Usuário encontrado!")

    # else:
    #     st.error("este usuário não está cadastrado!")

    st.markdown("# Aplicação de AEDA")

    # file = st.file_uploader("Suba seu arquivo csv aqui",type=['csv'])
    file = 'wine.csv'
    if file:
        df = pd.read_csv(file)

        st.dataframe(df.head())

        st.table(df.describe().transpose())

        plt.figure(figsize=(8,6))
        plt.scatter(df['fixed acidity'],df['volatile acidity'],s=4)
        plt.title('Verificação de Acidez')
        plt.xlabel('Acidez Fixa')
        plt.ylabel('Acidez Volátil')
        st.pyplot(plt.gcf())
        

if __name__ == '__main__':
    main()