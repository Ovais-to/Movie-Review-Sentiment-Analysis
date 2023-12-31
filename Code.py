# -*- coding: utf-8 -*-
"""Code

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16T9-Xszb0dkA8DP5UdO2dpN415y2YPtE
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
import seaborn as sns

"""# Loading and Viewing Dataset"""

df = pd.read_csv("IMDB Dataset.csv", on_bad_lines='skip')
df.head()

"""# Performing EDA"""

df.shape

df.isnull().sum()

df.info()

df['sentiment'].unique()

df['sentiment'].value_counts()

sns.catplot(x='sentiment', kind='count', data=df)

"""# Label Encoding"""

label = LabelEncoder()
df['sentiment'] = label.fit_transform(df['sentiment'])

df.head()

"""# Dividing The Dependent & Independent"""

x = df['review']
y = df['sentiment']

"""# Removing all the Characters and Special Characters from the Dataset"""

ps = PorterStemmer()
corpus = []

nltk.download('stopwords')

for i in range(len(x)):
  print(i)
  review = re.sub("[^a-zA-Z]"," ", x[i])
  review = review.lower()
  review = review.split()
  review = [ps.stem(word) for word in review if word not in set(stopwords.words("english"))]
  review = " ".join(review)
  corpus.append(review)

corpus

"""# Making text Data into Vectors using TfidfVectorizer"""

from sklearn.feature_extraction.text import TfidfVectorizer
cv = TfidfVectorizer(max_features = 5000)
x = cv.fit_transform(corpus).toarray()

x.shape

"""# Splitting Data into Train & Test"""

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 101)

x_train.shape, x_test.shape, y_train.shape, y_test.shape

"""# Define Naive Bayes Model"""

mnb = MultinomialNB()
mnb.fit(x_train, y_train)

"""# Testing Model Using Test Data"""

pred = mnb.predict(x_test)

"""# Checking Accuracy Score, Confusion Matrix & Classification Report"""

print(accuracy_score(y_test, pred))
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

"""# Differences Between Actual & Predicted Data"""

pd.DataFrame(np.c_[y_test,pred], columns = ["Actual", "Predicted"])

"""# Saving the Trained Naive-Bayes Model & TfidVectorizer"""

pickle.dump(cv, open("count-vectorizer.pkl", "wb"))
pickle.dump(mnb, open("Movies_Review_Classification.pkl", "wb"))

"""# Loading my Naive Bayes Model & TfidVectorizer"""

save_cv = pickle.load(open('count-vectorizer.pkl', 'rb'))
model = pickle.load(open('Movies_Review_Classification.pkl', 'rb'))

"""# Defining a function to Pre-Process the Review"""

def preprocess_review(review, vectorizer):
    review = re.sub("[^a-zA-Z]", " ", review)
    review = review.lower().split()
    review = [ps.stem(word) for word in review if word not in set(stopwords.words("english"))]
    review = " ".join(review)
    vectorized_review = vectorizer.transform([review]).toarray()
    return vectorized_review

"""# Defining a function to get user review and predict"""

def get_user_review_and_predict(model, vectorizer):
    user_review = input("Please write a movie review: ")
    preprocessed_review = preprocess_review(user_review, vectorizer)
    prediction = model.predict(preprocessed_review)[0]
    if prediction == 1:
        return "Positive Review"
    else:
        return "Negative Review"

"""# Result"""

prediction = get_user_review_and_predict(model, save_cv)
print(prediction)