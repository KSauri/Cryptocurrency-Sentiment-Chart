var MarketPrices = require('../models/marketPrice');
var moment = require('moment')


// TODO - change this so
// that on connection, you send the data
// and then emit events as you go
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
                    timestamp: price.timestamp,
                    marketCap: price.market_cap
                }
            ));

            res.send(JSON.stringify(formattedMarketPrices));
        });
};