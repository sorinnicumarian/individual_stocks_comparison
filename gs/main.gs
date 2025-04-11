function getStockPriceByParameter(apiKey, symbol, param) {
  if (!apiKey || !symbol || !param) {
    Logger.log("Error: Missing required parameters.");
    return "Error: Missing required parameters.";
  }

  try {
    var base_finnhub_url = "https://finnhub.io/api/v1/quote";
    var request_url = base_finnhub_url + "?symbol=" + symbol + "&token=" + apiKey;
    const response = UrlFetchApp.fetch(request_url);
    const jsonData = JSON.parse(response.getContentText());

    // Check if the API response contains valid data
    if (jsonData.o === undefined) {
      Logger.log("Error: Invalid API response.");
      return "Error: Invalid API response.";
    }

    // Extract the relevant data from the JSON response
    const { o: openPrice, h: highPrice, l: lowPrice, c: currentPrice, pc: previousClose } = jsonData;

    // Create a map for easier access to parameters
    const dataMap = {
      'open': openPrice,
      'high': highPrice,
      'low': lowPrice,
      'current': currentPrice,
      'previousClose': previousClose
    };

    // Check if the requested parameter is available in the dataMap
    if (!dataMap[param]) {
      Logger.log("Error: Invalid parameter requested.");
      return "Error: Invalid parameter requested.";
    }

    // Get the requested parameter
    const result = `${param.charAt(0).toUpperCase() + param.slice(1)} price for ${symbol}: $${dataMap[param].toFixed(2)}`;

    // Log the result for debugging purposes
    Logger.log(result);

    return result;  // Return the requested parameter

  } catch (error) {
    // Catch any errors during the API call
    Logger.log("Error: " + error.message);
    return "Error: " + error.message;
  }
}

function getStockInfo(apiKey, symbol) {

  if (!apiKey || !symbol) {
    Logger.log("Error: Missing required parameters.");
    return "Error: Missing required parameters.";
  }

  try {
    var base_finnhub_url = "https://finnhub.io/api/v1/quote";
    var request_url = base_finnhub_url + "?symbol=" + symbol + "&token=" + apiKey;
    const response = UrlFetchApp.fetch(request_url);
    const jsonData = JSON.parse(response.getContentText());

    // Check if the API response contains valid data
    if (jsonData.o === undefined) {
      Logger.log("Error: Invalid API response.");
      return "Error: Invalid API response.";
    }

    // Extracting the relevant data
    const { o: openPrice, h: highPrice, l: lowPrice, c: currentPrice, pc: previousClose } = jsonData;

    // Create a formatted result
    const result = `
      Stock Data for ${symbol}:
      - Open Price: $${openPrice.toFixed(2)}
      - High Price: $${highPrice.toFixed(2)}
      - Low Price: $${lowPrice.toFixed(2)}
      - Current Price: $${currentPrice.toFixed(2)}
      - Previous Close: $${previousClose.toFixed(2)}
    `;

    // Log the result for debugging purposes
    Logger.log(result);

    return result;  // Return the formatted result
  } catch (error) {
    // Catch any errors during the API call
    Logger.log("Error: " + error.message);
    return "Error: " + error.message;
  }
}