import pandas as pd
from pydataset import data


if __name__ == '__main__':
    titanic = data('titanic')

    print(titanic.sample(5))
    dados = {
        'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
        'Idade': [25, 30, 21, 29],
        'Gênero': ['Masculino', 'Feminino', 'Masculino', 'Feminino']
    }

    dataset = pd.DataFrame(dados)

    test  = pd.get_dummies(dataset, drop_first= True)

