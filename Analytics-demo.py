import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse

from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier


def data_classify_and_preidct():
    data = make_blobs(n_samples=200, centers=5, random_state=8)
    x, y = data

    # print(x)
    # print(x[:, 0])
    # print(y)

    clf = KNeighborsClassifier()
    clf.fit(x, y)

    x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
    y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1

    # print(np.arange(x_min, x_max, .02))
    # print("--" * 40)

    xx, yy = np.meshgrid(np.arange(x_min, x_max, .02),
                         np.arange(y_min, y_max, .02))

    # print(xx)
    # print("--" * 40)
    # print(yy)

    z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    z = z.reshape(xx.shape)
    # print(z)

    plt.pcolormesh(xx, yy, z, cmap=plt.cm.winter)


    plt.title("Classify: KNN")
    plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.spring, edgecolors="k")

    # plt.xlim(xx.min(), xx.max())
    # plt.ylim(yy.min(), yy.max())
    plt.scatter(6.75, 4.82, marker="*", c="red", s=300)
    plt.show()

    print(clf.predict([[6.75, 4.82]]))
    print(clf.score(x, y))


from sklearn.datasets import make_regression
from sklearn.neighbors import KNeighborsRegressor
def data_regression():
    x, y = make_regression(n_features=1, n_informative=1, noise=50, random_state=8)

    reg = KNeighborsRegressor(n_neighbors=2)
    reg.fit(x, y)
    z = np.linspace(-3, 3, 200).reshape(-1, 1)
    # print(z)
    plt.scatter(x, y, c="orange", edgecolors="k")
    plt.plot(z, reg.predict(z), c="k", linewidth=3)
    plt.title("KNN: regression")
    plt.show()

    print(reg.score(x, y))


from  sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
def wine_analysic():
    wine_sets = load_wine()
    print(wine_sets["data"].shape)
    print(wine_sets["DESCR"])


def demo():
    data = make_blobs(n_samples=200, centers=2, random_state=8)
    x, y = data

    plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.spring, edgecolors="k")
    plt.show()

    i = np.array([[1, 2, 3], [4, 5, 6]])
    print("i:\n{}".format(i))

    matrix = np.eye(6)
    print(matrix)

    sp = sparse.csr_matrix(matrix)
    print(sp)

    x = np.linspace(-20, 20, 10)
    y = x**3 + 2 * x**2 + 6 * x + 5

    plt.plot(x, y, marker=0)
    plt.show()


# data_classify_and_preidct()
# data_regression()
wine_analysic()