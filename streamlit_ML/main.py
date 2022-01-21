import streamlit as st
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


st.title("Test")

st.write("""
# Test different classifiers
Choose different sets.
""")


dataset_name = st.sidebar.selectbox("Choose DataSet", ("Iris", "Breast Cancer", "Wine"))
classifier_name = st.sidebar.selectbox("Choose Classifier", ("KNN", "SVM", "Random Forest"))


def get_dataset(dataset_name):
    if dataset_name == "Iris":
        data = datasets.load_iris()
    elif dataset_name == "Breast Cancer":
        data = datasets.load_breast_cancer()
    else:
        data = datasets.load_wine()
    X = data.data
    Y = data.target
    return X, Y

X, Y = get_dataset(dataset_name)
st.write("Dataset shape", X.shape)
st.write("number of classes", len(np.unique(Y)))

def add_ui(clf_name):
    param = dict()
    if clf_name == "KNN":
        K = st.sidebar.slider("K", 1, 20)
        param["K"] = K
    elif clf_name == "SVM":
        C = st.sidebar.slider("C", 0.01, 10.0)
        param["C"] = C
    else:
        max_depth = st.sidebar.slider("max_depth", 2, 20)
        n_estimators = st.sidebar.slider("n_estimators", 1, 50)
        param["max_depth"] = max_depth
        param["n_estimators"] = n_estimators
    return param

param = add_ui(classifier_name)

def get_class(clf_name, param):
    if clf_name == "KNN":
        clf = KNeighborsClassifier(n_neighbors=param["K"])
    elif clf_name == "SVM":
        clf = SVC(C = param["C"])
    else:
        clf = RandomForestClassifier(n_estimators=param["n_estimators"], max_depth=param["max_depth"], random_state=420)
    return clf

clf = get_class(classifier_name, param)