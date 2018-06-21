from sklearn import datasets, metrics
from sklearn import cross_validation as cv
from sklearn.naive_bayes import GaussianNB

# Loading the dataset
irisdataset = datasets.load_iris()

model = GaussianNB()
# getting the data and response of the dataset
x = irisdataset.data
y = irisdataset.target
# model.fit(x,y)
# print(model)
# model.predict(x,y)

splits = cv.train_test_split(x,y,test_size=0.2)
# target_names = ['class 0', 'class 1', 'class 2']
X_train, X_test, y_train, y_test =splits
#print(splits)
model.fit(X_train,y_train)
expected = y_test
print(expected)
predicted = model.predict(X_test)
print(predicted)
print("----")
# The classification_report function builds a text report showing the main classification metrics
#The support is the numaber of occurrences of each class in expected_true
#The precision is the ratio tp / (tp + fp)
#The recall is the ratio tp / (tp + fn)
#The F-beta score can be interpreted as a weighted harmonic mean of the precision and recall
print(metrics.classification_report(expected,predicted))
print("----")
print(metrics.confusion_matrix(expected,predicted))
print("----")

# The F1 score can be interpreted as a weighted average of the precision and recall, where an F1 score reaches its best value at 1 and worst score at 0.
# The relative contribution of precision and recall to the F1 score are equal. The formula for the F1 score is:
# F1 = 2 * (precision * recall) / (precision + recall)
print(metrics.f1_score(expected,predicted, average='micro'))