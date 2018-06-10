var express = require('express');
var router = express.Router();

// Require controller modules.
var coinController = require('../controllers/coinController');
var marketController = require('../controllers/marketController');
var sentimentController = require('../controllers/sentimentController');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

// get details for a coin by name
router.get('/coin/:name', coinController.coinDetail);

// get information about the overall market
router.get('/market', marketController.marketList);

// get reddit sentiment data
router.get('/sentiment', sentimentController.sentimentList);

module.exports = router;
