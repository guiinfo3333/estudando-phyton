from sklearn.neighbors import KNeighborsClassifier

if __name__ == '__main__':
    # Dados fictícios - características dos jogos de futebol
    # [Força do time casa, Força do time visitante, Local da partida (Casa = 1, Fora = 0), Resultado (Casa = 1, Fora = 0, Empate = 2)]
    dados = [
        [8, 6, 1, 1],  # Força do time casa: 8, Força do time visitante: 6, Local: Casa, Time da casa ganhou
        [5, 7, 0, 0],  # Força do time casa: 5, Força do time visitante: 7, Local: Fora, Time visitante ganhou
        [3, 5, 1, 2],  # Empate
        [9, 8, 0, 2],  # Empate
        [6, 7, 1, 0],  # Fora
        [7, 7, 0, 1],  # Casa
        [5, 6, 1, 2],  # Empate
        [8, 8, 0, 1]  # Casa
    ]

    # Classes correspondentes aos resultados dos jogos
    classes = ['Casa', 'Fora', 'Empate', 'Empate', 'Fora', 'Casa', 'Empate', 'Casa']

    # Criar modelo KNN
    knn = KNeighborsClassifier(n_neighbors=3)

    # Separar características (X) e alvos (y)
    X = [row[:3] for row in dados]  # Características: Força do time casa, Força do time visitante, Local da partida
    y = [row[3] for row in dados]  # Alvos: Resultado (Casa = 1, Fora = 0, Empate = 2)

    # Treinar o modelo
    knn.fit(X, y)

    # Novo jogo a ser previsto
    novo_jogo = [
        [7, 6, 1],  # Força do time casa: 6, Força do time visitante: 7, Local: Casa
    ]

    # Prever o resultado do novo jogo
    resultado_previsto = knn.predict(novo_jogo)
    if resultado_previsto[0] == 1:
        print("Time da casa ganhou")
    elif resultado_previsto[0] == 0:
        print("Time visitante ganhou")
    else:
        print("Empate")

    # Estimar as probabilidades para cada classe
    probabilidades = knn.predict_proba(novo_jogo)
    print("Probabilidades:", probabilidades[0])