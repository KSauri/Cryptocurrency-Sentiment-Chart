var MarketPrices = require('../models/marketPrice');
var moment = require('moment')


// list details of the overall crypto market
exports.marketList = function(req, res) {
    // set headers to be json    
    res.setHeader('Content-Type', 'application/json');
    
    var now = Date.now()
    var weekAgo = moment(now).subtract(7, 'days')
    
    MarketPrices.find({
        timestamp: {
          $gte: weekAgo.toDate(),
          $lt: now
        }
      })
        .exec(function (err, marketPrices) {
        if (err) { return next(err); }
            //Successful, so render
            let formattedMarketPrices = marketPrices.map(price => (
                {
                    coins: price.coins,
                    timestamp: price.timestamp,
                    marketCap: price.marketCap
                }
            ));

            res.send(JSON.stringify(formattedMarketPrices));
        });
};