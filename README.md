# Spam Detection using nltk library and Machine Learning Algorithm
## To used this project follow these steps
* Your system should contain pip as dependency
* Fork or download the code
* Create virtual env. inside Pycharm or visual studio
* fire this command pip install -r requirements.txt
* if above command run prefectly then run your app.py file
### Note to run this app locally make a small change in app.py
* remove this code app.run(host="0.0.0.0", port=port) with app.run(debug=True)
* remove this code port = int(os.getenv('PORT')) this is only for deployment server
## Algorithm Used
* To clean the text this code has been used
'''
 
        z = message
        l = []
        review = re.sub(r'\W+', ' ', z)
        review = review.lower()
        review = review.split()
        review = [lem.lemmatize(word) for word in review if word not in stop_words]
        review = ' '.join(review) has been used
        l.append(review)
        return l
 '''
 * Fot stemming WordNetLemmatizer() has been used
* To convert the text into numeric weight TFID algorithm has been used
* For classification naive  algorithm has been used you can also go with SVM
