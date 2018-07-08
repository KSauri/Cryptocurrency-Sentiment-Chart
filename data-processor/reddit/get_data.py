import os
from functools import reduce
import praw
from pymongo import MongoClient
import datetime

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

reddit = praw.Reddit(
    client_id=os.environ.get('REDDIT_ID'),
    client_secret=os.environ.get('REDDIT_SECRET'),
    password=os.environ.get('REDDIT_PASSWORD'),
    user_agent=os.environ.get('REDDIT_USER_AGENT'),
    username=os.environ.get('REDDIT_USERNAME')
)

# TODO introduce logging


class RedditCommentSentiment:
    """
    The Reddit class pulls streaming Reddit comments and assigns each comment
    a sentiment score.

    The `get()` method uses the current time and will return
    the average sentiment of all Reddit comments over an interval starting with the given time.
    """

    def __init__(self, duration=300):
        mongo_client =  MongoClient('mongodb://mongo:27017/mongo')
        db = mongo_client.mongo
        self._collection = db.commentsentiments
        self.timedelta = datetime.timedelta(seconds=duration)

    def _get_data(self):
        for comment in reddit.subreddit('all').stream.comments():
            yield comment.body

    def _get_score(self, reddit_comment):
        """
        `_get_score` gets a "polarity score" for a given piece of text.  
        This is a score from the nltk package that has scores for a given piece of text's "positivity", "negativity",
        and a "compouned" score that takes both into account.

        We use this "compound" score as a proxy for a given reddit comment's sentiment.

        Args:
            reddit_comment (str): a comment from reddit

        Returns:
            float: a value representing a given comment's sentiment score (from -1.0 to 1.0).
        """
        return sid.polarity_scores(reddit_comment)['compound']

    def _process_comments(self, finish_time):
        """
        _process_comments is the workhorse of the class.  It gets a "finish time" and pulls reddit comments until that
        finish time.

        It saves the data it gathers in a dict and returns the timestamp of the finish time as well as
        the average reddit sentiment over that time period.

        Args:
            None

        Returns:
            dict: a dictionary containing the average reddit sentiment for the given duration (defaults to 5 minutes)
                  as well as a timestamp for the end of the duration.
        """
        final_sentiment_data = {
            'avg_sentiment': 0.0,
            'timestamp': finish_time
        }
        sentiments = []
        comments = self._get_data()

        while datetime.datetime.utcnow() < finish_time:
            next_comment = next(comments)
            sentiments.append(self._get_score(next_comment))

        final_sentiment_data['avg_sentiment'] = reduce(lambda x, y: x + y, sentiments) / len(sentiments)
        return final_sentiment_data

    def get(self):
        """ 
        `get()` will fetch the average sentiment over a window of time (defaults to 5 minutes),
        starting immediately and ending at the current time + (duration).

        Args:
            None

        Returns:
            dict: a dictionary containing information about the sentiment of reddit comments for the past 5 minutes.
        """
        # TODO log the time
        timestamp = datetime.datetime.utcnow()
        finish_time = timestamp + self.timedelta
        return self._process_comments(finish_time)

    def save(self, reddit_data):
        self._collection.insert_one(reddit_data)
        return True