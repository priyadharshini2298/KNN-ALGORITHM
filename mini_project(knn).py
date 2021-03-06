# -*- coding: utf-8 -*-
"""Mini project(KNN).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nI13NN2lfScyZKbkc-a0ydBd1M4vp-n9
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files
uploaded= files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

# Commented out IPython magic to ensure Python compatibility.
# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

# Importing the dataset
dataset = pd.read_csv("student performance prediction MP.csv")
X = dataset.iloc[:, [0, 3]].values
print(X)
plot1 = dataset.iloc[:,[0]].values
print(plot1)

y = dataset.iloc[:, -1].values
print(y)

dataset.info()

import matplotlib.pyplot as plt
count =pd.value_counts(dataset["Result"], sort=False)
count.plot(kind= 'bar', color= ["blue", "red","green"])
plt.title('bar chart')
plt.legend(loc='best')
plt.show()

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the K-NN model on the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'euclidean', p = 2)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
print(y_pred)
print(y_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score,classification_report
cm = confusion_matrix(y_test, y_pred)
ac = accuracy_score(y_test, y_pred)
print(cm)
print(ac)
print ('Classification Report : ')
print (classification_report(y_test, y_pred))