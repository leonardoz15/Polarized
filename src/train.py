import sklearn
from sklearn import svm
from sklearn import datasets
from sklearn import metrics
import pandas as pd

# Import general-tweets.txt as tab-delimited csv
general_tweets = pd.read_csv("../data/general-tweets.txt", sep="\t", header=None)
# Set column headers
general_tweets.columns = ['subject', 'tweet']


# replace subject with dummy var, 0 = NOT, 1 = POLIT
general_tweets = general_tweets.replace(to_replace ="NOT", value = 0)
general_tweets = general_tweets.replace(to_replace ="POLIT", value = 1)

# cancer = datasets.load_breast_cancer()
#
# print(cancer.target_names)
# Features = tweet
x = general_tweets["tweet"]
# Target = subject
y = general_tweets["subject"]

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.2)

clf = svm.SVC(kernel="linear")
clf.fit(x_train, y_train)

# y_predict = clf.predict(x_test)
#
# acc = metrics.accuracy_score(y_test, y_predict)
#
# print(acc)
