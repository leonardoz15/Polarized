import sklearn
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import matplotlib.pyplot as plt

class TrainingML(object):
    '''
    Class for handling of both supervised models
    '''
    def __init__(self):
        '''
        Class constructor for initialization
        '''
        # import datasets, call training
        combined_tweets = pd.read_csv("../data/combined-tweets.txt", sep="\t", header=None)
        combined_tweets.columns = ['subject', 'tweet']

        # Features = tweet
        x = combined_tweets["tweet"]
        # Target = subject
        y = combined_tweets["subject"]

        clf_NB = trainingNB(combined_tweets)
        clf_SVM = trainingSVM(combined_tweets)

    def trainingNB(self, data):
        '''
        Utility function for training Multinomial NB based on combined dataset
        '''
        # Vectorize textual data
        tfidf = TfidfVectorizer(sublinear_tf=True, min_df=3, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')
        # Split into training and testing sets, and fit model
        X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.2)
        X_train_tfidf = tfidf.fit_transform(X_train)
        # Multinomial Naive Bayes
        clf = MultinomialNB().fit(X_train_tfidf, y_train)

        return clf

    def trainingSVM(self, data):
        '''
        Utility function for training linear SVM based on combined dataset
        '''
        # Vectorize textual data
        tfidf = TfidfVectorizer(sublinear_tf=True, min_df=3, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')
        # Split into training and testing sets, and fit model
        X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.2)
        X_train_tfidf = tfidf.fit_transform(X_train)
        # Linear SVM with regulization parameter
        clf = svm.SVC(kernel="linear", C=2)
        clf.fit(X_train_tfidf, y_train)

        return clf

    def predict_and_label(self, tweet):
        '''
        Utility function for predicting political subjectivity of each tweet
        '''
        label_NB = clf_NB.predict(tfidf.transform([tweet]))

        label_SVM = clf_SVM.predict(tfidf.transform([tweet]))

        # labels tweet as political or not, returns subject for both models
        # list returned, index 0 = NB index 1 = SVM
        list = [label_NB, label_SVM]
        
        return list




# y_predict = clf.predict(count_vect.transform(X_test))
# y_predict2 = clf2.predict(count_vect.transform(X_test))
#
# print(classification_report(y_test, clf2.predict(count_vect.transform(X_test))))
#
# accNB = metrics.accuracy_score(y_test, y_predict)
# accSVM = metrics.accuracy_score(y_test, y_predict2)
# print("Accuracy NB : ", accNB, "\nAccuracy SVM : ", accSVM)
