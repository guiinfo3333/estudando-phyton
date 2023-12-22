from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    def prever_resultado(dados, resultado):
        # dados: matriz contendo estatísticas dos jogos anteriores e indicador se o time da casa (time A) ganhou, perdeu ou empatou
        # resultado: lista indicando se o time da casa perdeu (0), empatou (1) ou venceu (2)

        # Dividir os dados em conjuntos de treino e teste
        X_train, X_test, y_train, y_test = train_test_split(dados, resultado, test_size=0.2, random_state=42)

        # Inicializar e treinar o modelo de regressão logística
        modelo = LogisticRegression(multi_class='multinomial', solver='lbfgs')
        modelo.fit(X_train, y_train)

        # Fazer previsões no conjunto de teste



        # dados do jogo que eu quero sabe ro resultado
        previsoes = modelo.predict([1, 0, 3, 2])
        return previsoes


    # Exemplo de dados históricos (estatísticas de jogos anteriores e indicador se o time da casa (time A) ganhou, perdeu ou empatou)
    # Vamos supor que temos 10 jogos e as estatísticas são representadas como matriz
    # As colunas são: gols_time_a, gols_time_b, posse_de_bola_time_a, posse_de_bola_time_b
    dados = [
        [1, 0, 3, 2],  # Estatísticas do jogo 1 (time A vs time B)
        [2, 1, 2, 2],  # Estatísticas do jogo 2 (time A vs time B)
        [0, 1, 1, 3],  # Estatísticas do jogo 3 (time A vs time B)
        [3, 0, 4, 1],  # Estatísticas do jogo 4 (time A vs time B)
        [1, 1, 2, 2],  # Estatísticas do jogo 5 (time A vs time B)

        [2, 0, 3, 1],  # Estatísticas do jogo 6 (time A vs time B)
        [0, 2, 2, 4],  # Estatísticas do jogo 7 (time A vs time B)
        [1, 0, 3, 1],  # Estatísticas do jogo 8 (time A vs time B)
        [2, 0, 3, 1],  # Estatísticas do jogo 9 (time A vs time B)
        [1, 1, 2, 2],  # Estatísticas do jogo 10 (time A vs time B)
    ]

    # Exemplo de resultados (0 para derrota  da casa , 1 para empate da casa , 2 para vitória da casa)
    resultado = [2, 2, 0, 2, 1, 2, 0, 2, 2, 1]

    # Chamando a função para fazer previsões
    previsoes = prever_resultado(dados, resultado)
    print("Previsões:", previsoes)