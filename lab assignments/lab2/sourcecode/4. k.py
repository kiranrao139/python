# importing all the sklearn packages
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import neighbors,datasets

# loading iris datasets
data_set = datasets.load_iris()

# loading data & target into x and y
x=data_set.data
y=data_set.target

#splitting training & testing data into x and y
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.2, random_state=22)

#defining the kmean
kmean=neighbors.KNeighborsClassifier(n_neighbors=10)

#fitting training data into kmeanmodel
kmean.fit(train_x, train_y)

#predicting kmean for test data
predicted_value=kmean.predict(test_x)

#Finally calculating the accuracy score using kmean model
print("Accuracy is: :", accuracy_score(predicted_value, test_y))
