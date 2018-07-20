import pandas as pd, numpy, pickle
from sklearn import model_selection, preprocessing, metrics, linear_model, svm, ensemble
from sklearn.externals import joblib

input_file = "authors.csv"
df = pd.read_csv(input_file, header = 0)
test_file = "testing.csv"
df1 = pd.read_csv(test_file, header = 0)


encoder = preprocessing.LabelEncoder()
train_lab = encoder.fit_transform(df['author'])
train_data = df.iloc[:,1:]
test_data = df1.iloc[:,1:]
test_lab = encoder.fit_transform(df1['author'])
def train(classifier, train_features, train_label, test_features):
    model = classifier.fit(train_features, train_label)# model

    preds = model.predict(test_features)#preds = predicted values
    print(preds)
    return metrics.accuracy_score(preds, test_lab)

accuracy = train(ensemble.RandomForestClassifier(n_estimators = 1000), train_data, train_lab , test_data)
print ("Random_Forest:", accuracy)


#get model, then implement:
#import pickle
#s = joblib.dump(model, "file.pkl")


#model2 = joblib.load("file.pkl")
#model2.predict(test_data)
