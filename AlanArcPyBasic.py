# AlanArcPyBasic.py
# Author: Alan Venneman
# Date: December 17, 2018
# Purpose: Uses basic ArcPy functions to set up the GIS environment, check if a shapefile exists, and print some
# properties of the shapefile.
# Inputs/Outputs: None
##################################################

# Import Modules
import arcpy

# Set up GIS environment
strENV = r"C:\Student\ICTPythonGIS\Data\Texas"
arcpy.env.workspace = strENV
arcpy.env.overwriteOutput = 0

# Check existence of shapefile
strShp = "JD_Contours.shp"
if arcpy.Exists(strShp):
    print("Huzzah")
else:
    print("Boo!")

# Print properties of a shapefile
desc = arcpy.Describe(strShp)
print(desc.datasetType)
print(desc.shapeType)

# Delete variables
del strENV, strShp
