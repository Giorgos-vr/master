from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer


cancer = load_breast_cancer()
X_train, X_test, Y_train, Y_test = train_test_split(cancer.data, cancer.target, random_state=0)
svc = SVC()
svc.fit(X_train, Y_train)

print(f"Accuracy on training set {svc.score(X_train, Y_train):.2f}\n")


#############

min_train = X_train.min(axis=0)
range_train = (X_train - min_train).max(axis=0)
X_train_scaled = (X_train - min_train) / range_train
X_test_scaled = (X_test - min_train) / range_train
svc = SVC()
svc.fit(X_train_scaled, Y_train)
print(f"Accuracy on training set after normalising {svc.score(X_train_scaled, Y_train):.2f}\n")
svc.score(X_train_scaled, Y_train)
print(f"Accuracy on test set after normalising {svc.score(X_test_scaled, Y_test):.2f}\n")