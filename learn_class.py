import pandas as pd
from sklearn import preprocessing, ensemble
from sklearn.externals import joblib

input_file = "author.csv"
df = pd.read_csv(input_file, header = 0)
test_file = "testing.csv"
df1 = pd.read_csv(test_file, header = 0)


encoder = preprocessing.LabelEncoder()
train_lab = df['author']
train_data = df.iloc[:,1:]
test_data = df1.iloc[:,1:]
test_lab = df1['author']
RFC = ensemble.RandomForestClassifier(n_estimators = 1000)
model = RFC.fit(train_data, train_lab)# model

preds = model.predict(test_data)#preds = predicted values
print(preds)



#get model, then implement:
s = joblib.dump(model, "file.pkl")



#put in 2nd file of code

import pandas as pd
from sklearn import preprocessing, ensemble
from sklearn.externals import joblib
test_file = "testing.csv"
df1 = pd.read_csv(test_file, header = 0)
test_data = df1.iloc[:,0:]
model2 = joblib.load("file.pkl")
preds2 = model2.predict(test_data)
return(preds2[0])
