var mongoose = require('mongoose');

var Schema = mongoose.Schema;

var coinSchema = new Schema(
  {
    name: {type: String, required: true, max: 100},
    price: {type: Number, required: true},
    rank: {type: Number, required: true},
    marketCap: {type: Number, required: true},
    timestamp: {type: Date, required: true}
  }
);

//Export model
module.exports = mongoose.model('CoinPrice', coinSchema);