# importing sklearn packages
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
# Implementing Naïve Bayes method using scikit-learn library
from sklearn.model_selection import train_test_split

#loading iris dataset available in the package
irisdatasets=datasets.load_iris()
x=irisdatasets.data
y=irisdatasets.target

#splitting the data for training and testing
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

# using gaussian formula
model=GaussianNB()
model.fit(x,y).predict(x)
print(model.score(x,y))

# using cross validation
mod = GaussianNB()
mod.fit(x,y)
print(mod.score(x_train,y_train))