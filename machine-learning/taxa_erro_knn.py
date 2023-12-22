import numpy as np
from sklearn import datasets
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


if __name__ == '__main__':
    iris = datasets.load_iris()
    irs = pd.DataFrame(iris.data, columns=iris.feature_names)
    irs['class'] = iris.target

    x = irs.iloc[:, :-1].values
    y = irs.iloc[:, 4].values


    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)
    scaler = StandardScaler()
    scaler.fit(x_train)

    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)

    error = []
    for i in range(1, 40):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(x_train, y_train)
        pred_i = knn.predict(x_test)
        error.append(np.mean(pred_i != y_test))


    #Plotando grafico com a taxa de erros
    plt.figure(figsize=(12, 6))
    plt.plot(
        range(1, 40),
        error, color='red',
        linestyle='dashed',
        marker='o',
        markerfacecolor='blue',
        markersize=10
    )
    plt.title('Error Rate K Value')
    plt.xlabel("K Value")
    plt.ylabel("Mean Error")

    plt.show()
