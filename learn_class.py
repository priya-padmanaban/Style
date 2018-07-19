import pandas as pd, numpy, pickle
from sklearn import model_selection, preprocessing, metrics, naive_bayes, svm
from sklearn.externals import joblib

input_file = "authors.csv"

df = pd.read_csv(input_file, header = 0)
print((df))
test_file = "testing.csv"
df1 = pd.read_csv(test_file, header = 0)


encoder = preprocessing.LabelEncoder()
train_lab = encoder.fit_transform(df[:,0])
train_data = df[:,1:]
test_data = df1[:,1:]
test_lab = encoder.fit_transform(df1[:,0])
def train(classifier, train_features, train_label, test_features):
    model = classifier.fit(train_features, train_label)# model

    preds = model.predict(test_data)#preds = predicted values
    return metrics.accuracy_score(preds, test_lab)

accuracy = train(naive_bayes.MultinomialNB(), train_data, train_lab , test_data)
print ("naive_bayes_Accuracy:", accuracy)

#get model, then implement:
#import pickle
#s = joblib.dump(model, "file.pkl")


#model2 = joblib.load("file.pkl")
#model2.predict(test_data)