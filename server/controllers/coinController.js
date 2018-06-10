var CoinPrices = require('../models/coinPrice');
var moment = require('moment')


// Display detail page for a specific Coin.
exports.coinDetail = function(req, res) {
    // set headers to be json
    res.setHeader('Content-Type', 'application/json');

    var now = Date.now()
    var weekAgo = moment(now).subtract(7, 'days')
    CoinPrices.find({
        timestamp: {
          $gte: weekAgo.toDate(),
          $lt: now
        },
        name: req.params.name
      })
        .exec(function (err, coinPrices) {
        if (err) { return next(err); }
        else if (!coinPrices.length) { 
            res.status(404).send('Not Found')
        } else {
            //Successful, so render
            let formattedCoinPrices = coinPrices.map(coinPrice => (
                {
                    name: coinPrice.name,
                    price: coinPrice.price,
                    rank: coinPrice.rank,
                    timestamp: coinPrice.timestamp,
                    marketCap: coinPrice.marketCap
                }
            ));
    
            res.send(JSON.stringify(formattedCoinPrices));
        }
        });
};

