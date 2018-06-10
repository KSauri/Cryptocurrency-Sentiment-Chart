var mongoose = require('mongoose');

var Schema = mongoose.Schema;

var sentimentSchema = new Schema(
  {
    sentiment: {type: Number, required: true},
    timestamp: {type: Date, required: true}
  }
);

//Export model
module.exports = mongoose.model('CommentSentiment', sentimentSchema);