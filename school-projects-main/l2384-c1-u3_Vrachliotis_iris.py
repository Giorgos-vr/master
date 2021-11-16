import pandas as pd
from urllib.request import urlretrieve

iris = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

urlretrieve(iris)
df = pd.read_csv(iris, sep=',')
col_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df.columns = col_names
#print(df.head(5))
mask_class = df['class'] == 'Iris-virginica'
df.loc[mask_class, 'class'] = "New label"
groupby_class_mean = df.groupby('class').mean()
print(groupby_class_mean)
#print(df)