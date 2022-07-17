import numpy as np
from sklearn.datasets import make_blobs


class LogisticRegression():
    def __init__(self, X, learning_rate=0.1, num_iters=10000):
        self.lr = learning_rate
        self.num_iters = num_iters
        self.m, self.n = X.shape  # m examples, n features

    def train(self, X, y):
        self.weights = np.zeros((self.n, 1))
        self.bias = 0

        for i in range(self.num_iters):
            # calculate the hypothesis:
            y_pred = self.sigmoid(np.dot(X, self.weights)+self.bias)
            # calculate cost
            cost = -1/self.m * np.sum(y*np.log(y_pred)+(1-y)*np.log(1-y_pred))
            # backprop
            dw = 1/self.m * np.dot(X.T, (y_pred-y))
            db = 1/self.m * np.sum(y_pred-y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            if i % 1000 == 0:
                print(f'Cost after iteration {i} : {cost}')

        return self.weights, self.bias

    def predict(self, X):
        y_predict = self.sigmoid(np.dot(X, self.weights)+self.bias)
        y_predict_labels = y_predict > 0.5

    def sigmoid(self, z):
        return 1/(1+np.exp(-z))


if __name__ == '__main__':
    np.random.seed(1)
    X, y = make_blobs(n_samples=1000, centers=2)
    y = y[:, np.newaxis]

    # logreg = LogisticRegression(X)
    # w, b = logreg.train(X, y)
    # y_pred = logreg.predict(X)

    # print(f'Accuracy: {np.sum(y==y_pred)/X.shape[0]}')
    l = ['Get', 'coffee', 'and', 'water', 'here']
    l2 = l[1:]
    l3 = l[1:4]
    print(l2)
    print(l3)
