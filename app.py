# importing the required libraries
from flask import Flask, render_template, request, redirect, url_for
from joblib import load

from get_tweet import fetch_tweets

# load the pipeline object
pipeline = load("tweetModel_V1.joblib")


# function to get results for a particular text query
def requestResults(name):
    # get the tweets text
    tweets = fetch_tweets(name)
    # get the prediction
    tweets['prediction'] = pipeline.predict(tweets['tweet_text'])
    # get the value counts of different labels predicted
    data = str(tweets.prediction.value_counts()) + '\n\n'
    return data + str(tweets)


# start flask
app = Flask(__name__)


# render default webpage
@app.route('/')
def home():
    return render_template('home.html')


# when the post method detect, then redirect to success function
@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name=user))


# get the data for the requested query
@app.route('/success/<name>')
def success(name):
    return "<xmp>" + str(requestResults(name)) + " </xmp> "


if __name__ == "__main__":
    app.run(debug=True)
    print("==============RUNNING DONE SUCCESSFULLY===========")

