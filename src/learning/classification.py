import random
import nltk
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000][1]


def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features


featuresets = [(document_features(d), c) for (d, c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)


print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)


# scklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.pipeline import Pipeline

vectorizer = TfidfVectorizer(
    preprocessor=lambda x: map(str, x),
    tokenizer=lambda x: x,
    ngram_range=(1, 3))

model = Pipeline([('vectorizer', vectorizer), ('model', MultinomialNB())])

from sklearn.svm import SVC

svm_model = Pipeline([('vectorizer', vectorizer), ('model', SVC())])

#