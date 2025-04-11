function testGetStockPriceByParameter() {
  var apiKeySheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Finnhub');
  var apiKey = apiKeySheet.getRange('B1').getValue(); // Get the API key from cell B1
  
  var symbol = "AAPL"; // Symbol for Apple (AAPL)
  var url = "https://finnhub.io/api/v1/quote"; // Base URL for Finnhub API

  // Testing different stock parameters
  var openPrice = getStockPriceByParameter(url, apiKey, symbol, 'o');
  Logger.log("Open Price: " + openPrice); // Expected: the open price of AAPL
  
  var highPrice = getStockPriceByParameter(url, apiKey, symbol, 'h');
  Logger.log("High Price: " + highPrice); // Expected: the high price of AAPL

  var lowPrice = getStockPriceByParameter(url, apiKey, symbol, 'l');
  Logger.log("Low Price: " + lowPrice); // Expected: the low price of AAPL

  var currentPrice = getStockPriceByParameter(url, apiKey, symbol, 'c');
  Logger.log("Current Price: " + currentPrice); // Expected: the current price of AAPL
  
  var previousClose = getStockPriceByParameter(url, apiKey, symbol, 'pc');
  Logger.log("Previous Close: " + previousClose); // Expected: the previous close price of AAPL
  
  // Testing with an invalid parameter
  var invalidParam = getStockPriceByParameter(url, apiKey, symbol, 'invalidParam');
  Logger.log("Invalid Parameter Test: " + invalidParam); // Expected: error message for invalid parameter
}

function testGetStockInfo() {
  var apiKeySheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Finnhub');
  var apiKey = apiKeySheet.getRange('B1').getValue(); // Get the API key from cell B1
  
  var symbol = "AAPL"; // Symbol for Apple (AAPL)
  
  getStockInfo(apiKey, symbol)
}

function simpleAPITest() {
  var apiKeySheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Finnhub');
  var apiKey = apiKeySheet.getRange('B1').getValue(); // Get the API key from cell B1
  
  var symbol = "AAPL"; // Symbol for Apple (AAPL)
  var url = "https://finnhub.io/api/v1/quote?symbol=" + symbol + "&token=" + apiKey;
  
  // Fetch the raw JSON data from the API
  var response = UrlFetchApp.fetch(url);
  var jsonData = JSON.parse(response.getContentText());
  
  // Log the raw response data to see if we get the expected data
  Logger.log(jsonData);
}