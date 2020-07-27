# importing the necessary dependencies
import os
import nltk
import pickle
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from DataPreprocessing.preprocessing import Preprocessing
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            message = (request.form['message'])
            p = Preprocessing(message)
            result = p.text_cleaning()
            print(result)
            cv = CountVectorizer(max_features=2500)
            filename = 'corpus.pickle'
            corpus = pickle.load(open(filename, 'rb'))
            cv.fit_transform(corpus).toarray()
            result = cv.transform(result).toarray()
            name = 'spam_model.pickle'
            model = pickle.load(open(name, 'rb'))
            predict = model.predict(result)
            label = predict[0]
            if label == 1:
                value='This is a SPAM Message Dear'
                return render_template('results.html',message=value)
            else:
                value= 'This is not a SPAM Message Dear'
                return render_template('results.html',message=value)

        except Exception as e:
            print('The Exception message is: ', e)
            return 'Something Went Wrong with server'
    # return render_template('results.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
