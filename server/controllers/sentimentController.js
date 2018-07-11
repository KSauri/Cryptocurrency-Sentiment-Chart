var CommentSentiment = require('../models/sentiment');
var moment = require('moment')


// TODO - change this so
// that on connection, you send the data
// and then emit events as you go
// list details of overall Reddit sentiment
exports.sentimentList = function(req, res) {
    // set headers to be json    
    res.setHeader('Content-Type', 'application/json');

    var now = Date.now()
    var weekAgo = moment(now).subtract(7, 'days')
    
    CommentSentiment.find({
        timestamp: {
            $gte: weekAgo.toDate(),
            $lt: now
        }
        })
        .exec(function (err, sentiments) {
        if (err) { return next(err); }
            //Successful, so render
            let formattedSentiments = sentiments.map(discreteSentiment => {
                return {
                    timestamp: discreteSentiment.timestamp,
                    sentiment: discreteSentiment.avg_sentiment, 
                }
            });

            res.send(JSON.stringify(formattedSentiments));
        });
};
