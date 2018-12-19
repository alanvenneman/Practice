# AlanConvertCoordinates.py
# Author: Alan Venneman
# Date: December 17, 2018
# Purpose: Prompts for an input and output datum and suggests a datum tranformation.
# Inputs: strInputDatum, strOutputDatum
# Outputs: Datum transformation method
##################################################
print("-" * 40)

# Retrieve input coordinates
strLon = raw_input("Enter Longitude: ")
strLat = raw_input("Enter Latitude: ")

## degLon = float(strLon[:3])
## minLon = float(strLon[4:6])
## secLon = float(strLon[7:])
# Use split instead of slice
degLon, minLon, secLon = strLon.split()
degLon = float(degLon)
minLon = float(minLon)
secLon = float(secLon)

## degLat = float(strLat[:2])
## minLat = float(strLat[3:5])
## secLat = float(strLat[6:])
# Again using split
degLat, minLat, secLat = strLat.split()
degLat = float(degLat)
minLat = float(minLat)
secLat = float(secLat)

# Calculate Decimal places
ddLon = degLon + minLon / 60 + secLon / 3600
ddLat = degLat + minLat / 60 + secLat / 3600

# Print Results
print("Lon: {}".format(ddLon))
print("Lat: {}".format(ddLat))

# Delete variables
del strLon, strLat, degLon, minLon, secLon, degLat, minLat, secLat, ddLon, ddLat
