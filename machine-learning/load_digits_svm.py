from sklearn import datasets
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn import svm

# Support Vector Machine
if __name__ == '__main__':

    digits = datasets.load_digits()

    plt.figure(figsize=(20, 4))

    #Colocando grafico
    # for index, (image, label) in enumerate(zip(digits.data[0:5], digits.target[0:5])):
    #     plt.subplot(1, 5, index + 1)
    #     plt.imshow(np.reshape(image, (8, 8)), cmap=plt.cm.gray)
    #     plt.title('Target: {}\n'.format(label, fontsize =20))
    # plt.show()

    #Implementando um estimador
    clf = svm.SVC(gamma=0.001, C= 100.)
    clf.fit(digits.data[:-1], digits.target[:-1])

    #Prevendo novos valores
    print(clf.predict(digits.data[-1:]))



    #Criar um SVM para cada partida
