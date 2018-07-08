var mongoose = require('mongoose');

var Schema = mongoose.Schema;

var marketSchema = new Schema(
  {
    market_cap: {type: Number, required: true},
    timestamp: {type: Date, required: true}
  }
);

//Export model
module.exports = mongoose.model('MarketPrice', marketSchema);