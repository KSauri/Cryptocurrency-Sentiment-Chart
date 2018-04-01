import os
import praw
import datetime

from functools import reduce
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


class Reddit:
    """
    The Reddit class pulls streaming Reddit comments and assigns each comment
    a sentiment score.

    The `get_data()` method returns a generator that provides access to streaming Reddit comments

    The `process_data()` method uses the instance variable `self.timestamp` and will return
    the average sentiment of a five minute interval starting with `self.timestamp` of all Reddit comments.
    """

    def __init__(self, timestamp):
        delta = datetime.timedelta(seconds=300)
        self.timestamp = timestamp
        self.finish_time = timestamp + delta

    def get_data(self):
        """
        TODO add docstring
        """
        for comment in reddit.subreddit('all').stream.comments():
            yield comment.body

    def _get_score(self, reddit_comment):
        return sid.polarity_scores(reddit_comment)['compound']

    def process_data(self):
        """
        TODO add docstring
        """
        final_sentiment_data = {
            'avg_sentiment': 0.0,
            'timestamp': str(self.timestamp)
        }

        sentiments = []
        comments = self.get_data()

        # NB while loop = super gross here
        # TODO swap out time.sleep() for while loop, or something else
        while datetime.datetime.now() < self.finish_time:
            next_comment = next(comments)
            sentiments.append(self._get_score(next_comment))

        final_sentiment_data['avg_sentiment'] = reduce(lambda x, y: x + y, sentiments) / len(sentiments)
        return final_sentiment_data
