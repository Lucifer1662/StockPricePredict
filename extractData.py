from convertStockToJson import getDataOfListings, getDataFileNames
from percentJson import percentJson, getPercentFileNames
from normalizeJson import normalizeJson, getNormalizeFileNames


getDataOfListings(None)
percentJson(getDataFileNames())
print("finish percent")
normalizeJson(getPercentFileNames())