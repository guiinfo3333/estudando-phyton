from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    iris = datasets.load_iris()
    irs = pd.DataFrame(iris.data, columns= iris.feature_names)
    irs['class'] = iris.target
    irs.head()
    # print(irs)

    # Implementacao NearestNeighbours
    x = irs.iloc[:, :-1].values
    y = irs.iloc[:, 4].values
    # print(x)
    # print(y)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)
    scaler = StandardScaler()
    scaler.fit(x_train)

    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)


    # Treinando o algoritmo Neighbors (Vizinhanca) com os dados x de teste e os dados y de tes
    classifier = KNeighborsClassifier(n_neighbors=9)
    classifier.fit(x_train, y_train)


    y_pred = classifier.predict(x_test)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
