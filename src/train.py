import sklearn
from sklearn import svm
from sklearn import datasets
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import matplotlib.pyplot as plt

# Import general-tweets.txt as tab-delimited csv
general_tweets = pd.read_csv("../data/general-tweets.txt", sep="\t", header=None)
# Set column headers
general_tweets.columns = ['subject', 'tweet']

# Import keyword-tweets.txt as tab-delimited csv
keyword_tweets = pd.read_csv("../data/keyword-tweets.txt", sep="\t", header=None)
# Set column headers
keyword_tweets.columns = ['subject', 'tweet']

# Import keyword-tweets.txt as tab-delimited csv
# extracted_tweets = pd.read_csv("../data/ExtractedTweets.csv")


fig = plt.figure(figsize=(8,6))
general_tweets.groupby('subject').tweet.count().plot.bar(ylim=0)
plt.show()

fig = plt.figure(figsize=(8,6))
keyword_tweets.groupby('subject').tweet.count().plot.bar(ylim=0)
plt.show()

# fig = plt.figure(figsize=(8,6))
# extracted_tweets.groupby('Party').Tweet.count().plot.bar(ylim=0)
# plt.show()

# replace subject with dummy var, 0 = NOT, 1 = POLIT
# general_tweets = general_tweets.replace(to_replace ="NOT", value = 0)
# general_tweets = general_tweets.replace(to_replace ="POLIT", value = 1)
#
# keyword_tweets = keyword_tweets.replace(to_replace ="NOT", value = 0)
# keyword_tweets = keyword_tweets.replace(to_replace ="POLIT", value = 1)

# Features = tweet
x = keyword_tweets["tweet"]
# Target = subject
y = keyword_tweets["subject"]

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=3, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')

features1 = tfidf.fit_transform(general_tweets.tweet).toarray()
print(features1.shape)

features2 = tfidf.fit_transform(keyword_tweets.tweet).toarray()
print(features2.shape)

# features3 = tfidf.fit_transform(extracted_tweets.Tweet).toarray()
# features3.shape
# print(features3)

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.2)
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)


string = "Pizza"
print("String to test :\n", string)

print("Testing with multinomial NB:")

# MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, y_train)
print(clf.predict(count_vect.transform([string])))

# Linear SVM with regulization parameter C
clf2 = svm.SVC(kernel="linear", C=2)
clf2.fit(X_train_tfidf, y_train)

print("Testing with linear SVM:")
print(clf2.predict(count_vect.transform([string])))

y_predict = clf.predict(count_vect.transform(X_test))
y_predict2 = clf2.predict(count_vect.transform(X_test))

print(classification_report(y_test, clf2.predict(count_vect.transform(X_test))))

accNB = metrics.accuracy_score(y_test, y_predict)
accSVM = metrics.accuracy_score(y_test, y_predict2)
print("Accuracy NB : ", accNB, "\nAccuracy SVM : ", accSVM)
