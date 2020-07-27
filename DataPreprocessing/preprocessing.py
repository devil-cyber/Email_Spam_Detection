import re
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer



class Preprocessing:
    def __init__(self, message):
        self.message = message

    def text_cleaning(self):
        lem = WordNetLemmatizer()
        stop_words = stopwords.words('english')


        z = self.message
        l = []
        review = re.sub(r'\W+', ' ', z)
        review = review.lower()
        review = review.split()
        review = [lem.lemmatize(word) for word in review if word not in stop_words]
        review = ' '.join(review)
        l.append(review)
        return l
