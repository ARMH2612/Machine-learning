import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import seaborn as sns


X, y = make_classification(n_samples=2000, n_features=2,
                           n_informative=2, n_redundant=0, n_classes=2, random_state=32)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=32)

svc_model = SVC(kernel='linear', random_state=32)
svc_model.fit(X_train, y_train)

plt.figure(figsize=(10, 8))
sns.scatterplot(x=X_train[:, 0], y=X_train[:, 1], hue=y_train, s=8)

w = svc_model.coef_[0]
b = svc_model.intercept_[0]
x_points = np.linspace(-1, 1)
y_points = -(w[0]/w[1]) * x_points - b / w[1]

plt.plot(x_points, y_points, c='r')

plt.scatter(svc_model.support_vectors_[:, 0], svc_model.support_vectors_[
            :, 1], s=50, facecolors='none', edgecolor='k', alpha=.5)

w_hat = svc_model.coef_[0] / (np.sqrt(np.sum(svc_model.coef_[0] ** 2)))
margin = 1/np.sqrt(np.sum(svc_model.coef_[0] ** 2))

decision_boundary_ponts = np.array(list(zip(x_points, y_points)))
points_of_line_above = decision_boundary_ponts + w_hat * margin
points_of_line_below = decision_boundary_ponts - w_hat * margin

plt.plot(points_of_line_above[:, 0],
         points_of_line_above[:, 1], 'b--', linewidth=2)
plt.plot(points_of_line_below[:, 0],
         points_of_line_below[:, 1], 'g--', linewidth=2)

plt.show()
